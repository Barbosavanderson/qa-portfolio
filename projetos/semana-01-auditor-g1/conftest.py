# conftest.py
import pytest
from playwright.sync_api import Page

# Fixture 1 — navega para o DuckDuckGo antes de cada teste
@pytest.fixture
def pagina_duckduckgo(page: Page):
    page.goto("https://duckduckgo.com")
    yield page

# Fixture 2 — dados de teste do PIX
@pytest.fixture
def dados_pix():
    return {
        "chave_valida": "vanderson@email.com",
        "valor_minimo": "0.01",
        "valor_maximo": "5000.00",
        "valor_acima_limite": "5000.01",
        "valor_zero": "0.00"
    }

# Fixture 3 — screenshot automático em falhas
@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request):
    yield
    if request.node.rep_call.failed:
        try:
            page.screenshot(
                path=f"screenshots/{request.node.name}.png",
                full_page=True
            )
        except Exception:
            pass  # se o browser já fechou, ignora silenciosamente