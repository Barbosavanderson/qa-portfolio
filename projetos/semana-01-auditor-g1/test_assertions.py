# test_assertions.py
import re
from playwright.sync_api import Page, expect

def test_busca_retorna_resultados(pagina_duckduckgo):
    # Act
    pagina_duckduckgo.get_by_placeholder("Pesquisar em privado").fill("Playwright Python QA")
    pagina_duckduckgo.get_by_placeholder("Pesquisar em privado").press("Enter")

    # Assert 1 — URL mudou
    expect(pagina_duckduckgo).not_to_have_url("https://duckduckgo.com/")

    # Assert 2 — URL contém o termo buscado
    expect(pagina_duckduckgo).to_have_url(re.compile(r"Playwright"))

    # Assert 3 — campo mantém o texto digitado
    expect(
        pagina_duckduckgo.get_by_placeholder("Pesquisar em privado")
    ).to_have_value("Playwright Python QA")

def test_busca_com_dados_pix(pagina_duckduckgo, dados_pix):
    chave = dados_pix["chave_valida"]

    pagina_duckduckgo.get_by_placeholder("Pesquisar em privado").fill(chave)
    pagina_duckduckgo.get_by_placeholder("Pesquisar em privado").press("Enter")

    expect(pagina_duckduckgo).not_to_have_url("https://duckduckgo.com/").
    #ttest