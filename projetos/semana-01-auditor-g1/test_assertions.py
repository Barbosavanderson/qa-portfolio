# # test_assertions.py
# import re
# from playwright.sync_api import Page, expect

# def test_busca_retorna_livros(page: Page):
#     # Arrange
#     page.goto("https://books.toscrape.com")

#     # Assert 1 — título da página está correto
#     expect(page).to_have_title(re.compile(r"Books"))

#     # Assert 2 — URL está na home
#     expect(page).to_have_url("https://books.toscrape.com/")

#     # Assert 3 — catálogo tem exatamente 20 livros na primeira página
#     expect(page.locator("article.product_pod")).to_have_count(20)

#     # Assert 4 — botão de próxima página está visível
#     expect(page.get_by_role("link", name="next")).to_be_visible()

#     # Assert 5 — título "1000 results" aparece na página
#     expect(page.get_by_text("1000 results")).to_be_visible()



# test_assertions.py
import re
from playwright.sync_api import Page, expect

def test_quebrar_titulo(page: Page):
    page.goto("https://books.toscrape.com")
    
    # ❌ Título errado de propósito
    expect(page).to_have_title("Amazon")

def test_quebrar_url(page: Page):
    page.goto("https://books.toscrape.com")
    
    # ❌ URL errada de propósito
    expect(page).to_have_url("https://books.toscrape.com/pagina-que-nao-existe")

def test_quebrar_contagem(page: Page):
    page.goto("https://books.toscrape.com")
    
    # ❌ Contagem errada de propósito — tem 20, estamos pedindo 99
    expect(page.locator("article.product_pod")).to_have_count(99)

def test_quebrar_texto(page: Page):
    page.goto("https://books.toscrape.com")
    
    # ❌ Texto que não existe na página
    expect(page.get_by_text("Texto que nao existe na pagina")).to_be_visible()

def test_quebrar_visibilidade(page: Page):
    page.goto("https://books.toscrape.com")
    
    # ❌ Elemento que não existe
    expect(page.get_by_role("button", name="Comprar agora")).to_be_visible()