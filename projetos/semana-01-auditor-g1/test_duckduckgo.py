# test_duckduckgo.py
from playwright.sync_api import Page, expect

def test_busca_retorna_resultados(page: Page):
    # Arrange — preparar
    page.goto("https://duckduckgo.com")

    # Act — agir
    page.get_by_placeholder("q").fill("Vanderson Barbosa")
    page.get_by_placeholder("q").press("Enter")

    # Assert — validar
    expect(page).not_to_have_url("https://duckduckgo.com/")
    expect(page.locator(".react-results--main")).to_be_visible()



    # NOTA: DuckDuckGo bloqueia acesso headless com timeout.
# Solução futura: usar --headed ou trocar para site sem anti-bot.
# Conceito validado: goto, get_by_placeholder, fill, press, expect.