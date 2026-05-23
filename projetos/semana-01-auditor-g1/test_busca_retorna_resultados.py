from playwright.sync_api import Page, expect
def test_busca_retorna_resultados(page: Page):

    # Arrange — preparar
    page.goto("https://www.google.com")

    #Fechar pop-up de cookies
    try:
        page.get_by_role("button", name="Não usar o chrome").click()
    except:
        pass
    # Act — o que vais ser feito
    page.keyboard.fill("spch", "Vanderson Barbosa")
    page.keyboard.press("Enter")

    #Assert URL mudou, saiu da home
    expect(page).not_to_have_url("https://www.google.com/")

    #Assert página de resultados carregou?
    expect(page.locator("#search")).to_be_visible()




    #retornou erro de timeout, provavelmente por bloqueio de bot. Solução futura: usar --headed ou trocar para site sem anti-bot. Conceito validado: goto, get_by_placeholder, fill, press, expect.