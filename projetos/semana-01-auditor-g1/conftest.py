import pytest

@pytest.fixture(autouse=True)
def screeshot_on_failure(page, request):
    yield # Executa o teste normalmente

    #roda se o teste falhar
    if request.node.rep_call.failed:
        # Salva o screenshot com o nome do teste
        page.screenshot(path=f"screenshots/{request.node.name}.png",
                        full_page=True
                        )
        @pytest.hookimpl(hookwrapper=True, tryfirst=True)
        def pytest_runtest_makereport(item, call):
            # Executa o teste e obtém o resultado
            outcome = yield
            rep = outcome.get_result()

            # Anexa o resultado do teste ao item para acesso posterior
            setattr(item, "rep_" + rep.when, rep)