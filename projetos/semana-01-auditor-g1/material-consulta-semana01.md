# Material de Consulta — Semana 1
**QA Portfolio — Vanderson Barbosa**  
Compilado dos dias 1 ao 4 · Atualizado conforme o plano avança

---

## Índice

1. [Dia 1 — SDLC, STLC, Tipos de Teste e Pirâmide](#dia-1--sdlc-stlc-tipos-de-teste-e-pirâmide)
2. [Dia 2 — Casos de Teste e Report de Bugs](#dia-2--casos-de-teste-e-report-de-bugs)
3. [Dia 3 — Git na prática](#dia-3--git-na-prática)
4. [Dia 4 — Playwright: instalação e primeiros conceitos](#dia-4--playwright-instalação-e-primeiros-conceitos)
5. [Exercícios realizados](#exercícios-realizados)
6. [Erros comuns e como resolver](#erros-comuns-e-como-resolver)

---

## Dia 1 — SDLC, STLC, Tipos de Teste e Pirâmide

### SDLC — Software Development Life Cycle
Ciclo de vida completo do software — do requisito ao deploy.

| Fase | O que acontece | Papel do QA |
|------|---------------|-------------|
| Requisitos | Define o que o sistema faz | Faz perguntas, levanta riscos |
| Design | Como será construído | Revisa fluxos, identifica riscos |
| Desenvolvimento | Devs escrevem o código | Prepara casos de teste |
| Testes | QA executa e reporta bugs | Execução, report, regressão |
| Deploy | Sistema vai para produção | Smoke test pós-deploy |
| Manutenção | Bugs e melhorias | Regressão contínua |

> **Shift Left:** quanto mais cedo o QA entra, mais barato é corrigir.  
> Bug nos requisitos = custa 1x · Bug em produção = custa 100x

---

### STLC — Software Testing Life Cycle
Ciclo de vida do processo de testes dentro do projeto.

```
Análise de requisitos
       ↓
  Planejamento
       ↓
Design dos casos de teste
       ↓
Configuração do ambiente
       ↓
    Execução
       ↓
  Encerramento
```

---

### Tipos de teste

| Tipo | O que é | Quando usar |
|------|---------|-------------|
| Funcional | Verifica se o sistema faz o que foi especificado | Todo ciclo |
| Regressão | Garante que mudanças não quebraram o que funcionava | Após qualquer mudança |
| Exploratório | Investigação criativa sem roteiro fixo | Descoberta de bugs ocultos |
| Smoke | Verificação rápida de que o build básico funciona | Antes de testar em profundidade |
| Sanidade | Confirma que um bug específico foi corrigido | Após correção de bug |

---

### Caixa Preta vs Caixa Branca

| | Caixa Preta | Caixa Branca |
|---|---|---|
| Vê o código? | Não | Sim |
| Foco | Entradas e saídas | Caminhos internos do código |
| Quem usa | QA em geral | QA técnico / devs |
| Exemplo | Login com email/senha → usuário entra | Cobertura de todos os if/else do método |

---

### Pirâmide de Testes

```
        /\
       /  \
      / E2E\          ← Poucos · lentos · caros
     /------\           Fluxo completo do usuário
    /        \          Ex: login → PIX → comprovante
   /Integração\       ← Volume médio · velocidade média
  /------------\        Comunicação entre componentes
 /              \       Ex: módulo pagamento ↔ banco de dados
/   Unitários    \    ← Muitos · rápidos · baratos
/________________\      Funções isoladas
                        Ex: calcular juros, validar CPF
```

**Regra de ouro:** quem inverte a pirâmide (muitos E2E, poucos unitários)
sofre com suítes lentas, instáveis e caras de manter.

**Analogia Naruto:**
- Unitários = Kage Bunshin — mil clones fazendo uma coisa isolada
- Integração = Time 7 — Naruto, Sasuke e Sakura trabalhando juntos
- E2E = Sage Mode — poderoso, raro, demorado de ativar

---

### Resumo Dia 1

| Conceito | Em uma frase |
|---|---|
| SDLC | Ciclo de vida completo do software |
| STLC | Ciclo de vida do processo de testes |
| Shift Left | QA entra cedo — prevenir é mais barato |
| Teste funcional | Verifica se o sistema faz o que foi especificado |
| Teste de regressão | Garante que mudanças não quebraram nada |
| Teste exploratório | Investigação criativa sem roteiro fixo |
| Smoke test | Verificação rápida do build básico |
| Caixa preta | Testa comportamento sem ver o código |
| Pirâmide de testes | Muitos unitários, poucos E2E |

---

## Dia 2 — Casos de Teste e Report de Bugs

### Anatomia de um caso de teste profissional

```
ID:           TC-PIX-001
Título:       [o que está sendo testado em uma frase]
Pré-condição: [o que precisa ser verdade ANTES de executar]
Passos:
  1. [ação única e específica]
  2. [ação única e específica]
  3. [ação única e específica]
Resultado esperado: [o que DEVERIA acontecer]
Resultado obtido:   [o que REALMENTE aconteceu — preenchido na execução]
Status:       PASS | FAIL
Evidência:    [screenshot ou vídeo descrito]
```

---

### Tipos de casos de teste — sempre cubra os 4

| Tipo | O que testa | Exemplo PIX |
|------|-------------|-------------|
| Caminho feliz | Fluxo ideal | Transferir R$ 100 com todos os dados corretos |
| Caso negativo | Erro do usuário | Transferir com saldo insuficiente |
| Caso de borda | Limites extremos | Transferir R$ 0,01 (mínimo) e R$ 5.000,00 (máximo) |
| Segurança básica | Inputs maliciosos | Campo valor com `<script>alert(1)</script>` |

> **Regra dos casos de borda:** sempre testam em pares — limite inferior E limite superior.

---

### Anatomia de um bug report profissional

```
ID:                BUG-PIX-004
Título:            [o quê] + [onde] + [condição]
                   Ex: "App fecha após confirmação de PIX no Android 12.1"

Severidade:        Crítico | Alto | Médio | Baixo
Prioridade:        Alta | Média | Baixa
Ambiente:          Device · OS · Versão do app · Ambiente (homologação/produção)

Pré-condição:      [estado do sistema antes de reproduzir]

Passos:
  1. [ação]
  2. [ação]
  3. [ação]

Resultado esperado: [o que deveria acontecer]
Resultado obtido:   [o que aconteceu de verdade]

Evidência:         [descrição do screenshot ou vídeo]
```

---

### Níveis de severidade

| Severidade | Analogia Demon Slayer | Quando usar |
|---|---|---|
| Crítico | Lua Superior — Kokushibo | Sistema inutilizável, perda de dados, segurança comprometida |
| Alto | Lua Inferior — Enmu | Funcionalidade principal quebrada, sem workaround |
| Médio | Demônio comum | Funcionalidade afetada mas existe alternativa |
| Baixo | Espírito fraco | Problema cosmético, texto errado, cor incorreta |

> **Atenção:** Severidade ≠ Prioridade.  
> Um botão com cor errada na tela de pagamento pode ter severidade Baixa mas prioridade Alta — impacta a marca.

---

### Título de bug — formato correto

```
❌ Errado:  "app quebrou"
❌ Errado:  "PIX com problema"
❌ Errado:  "login quebrado"

✅ Correto: "App fecha inesperadamente após confirmação de PIX no Android 12.1"
✅ Correto: "Sistema aceita email sem @ e avança no cadastro sem validar formato"
✅ Correto: "Transferência PIX de R$ 5.000,01 processada acima do limite permitido"

Formato: O QUÊ + ONDE + CONDIÇÃO
```

---

### Resumo Dia 2

| Campo | Para que serve |
|---|---|
| ID | Referenciar em relatórios e tickets |
| Pré-condição | Garantir que o ambiente está pronto |
| Passos | Reprodutibilidade sem perguntas |
| Resultado esperado | O contrato do sistema |
| Resultado obtido | A evidência do problema |
| Severidade | Impacto técnico |
| Prioridade | Urgência de correção |
| Evidência | Prova irrefutável |

---

## Dia 3 — Git na prática

### Por que QA precisa de Git
- Testes vivem no mesmo repositório que o código
- Portfólio no GitHub é currículo técnico
- Recrutador abre o perfil antes de ler o PDF

---

### Comandos essenciais

```bash
# Clonar repositório
git clone https://github.com/usuario/repo.git

# Ver o que mudou
git status

# Adicionar arquivos
git add nome-do-arquivo.md
git add .                    # adiciona tudo

# Criar commit
git commit -m "feat: adicionar casos de teste do fluxo PIX"

# Enviar para o GitHub
git push origin main

# Baixar mudanças do GitHub
git pull

# Criar branch e mudar para ela
git checkout -b nome-da-branch

# Ver branches existentes
git branch

# Voltar para a main
git checkout main

# Ver histórico de commits
git log --oneline
```

---

### Conventional Commits — padrão de mensagens

```
tipo: descrição curta no imperativo

feat:     novo caso de teste ou nova cobertura
fix:      correção de caso de teste errado
docs:     mudança no README ou documentação
test:     ajuste em automação
refactor: reorganização sem mudar comportamento
```

**Exemplos:**
```bash
git commit -m "feat: adicionar casos de teste do fluxo de transferência PIX"
git commit -m "docs: adicionar bug report BUG-PIX-004 app fecha após confirmação"
git commit -m "fix: corrigir pré-condição do caso TC-PIX-003"
```

---

### Estrutura de repositório QA

```
qa-portfolio/
├── README.md
├── casos-de-teste/
│   └── semana-01/
│       └── TC-PIX-transferencia.md
├── bugs/
│   └── BUG-PIX-004.md
├── projetos/
│   └── semana-01-auditor-g1/
└── .github/
    └── workflows/           ← CI/CD — semana 4
```

---

### Erros comuns no Git e como resolver

| Erro | Causa | Solução |
|---|---|---|
| `rejected — fetch first` | GitHub tem commits que você não tem local | `git pull origin main --allow-unrelated-histories` |
| `master vs main` | Branch criada diferente do padrão | `git branch -m master main` + `git push origin main` |
| `nothing to commit` | Arquivos não foram adicionados | `git add .` antes do commit |
| `detached HEAD` | Você está num commit solto | `git checkout main` |

---

### Resumo Dia 3

| Conceito | Em uma frase |
|---|---|
| Repositório | Pasta com histórico completo de mudanças |
| Commit | Foto do projeto com mensagem explicativa |
| Branch | Linha paralela de trabalho sem bagunçar a main |
| Push | Enviar do computador para o GitHub |
| Pull Request | Proposta de juntar uma branch com a main |
| Conventional Commits | Padrão: tipo: descrição curta |

---

## Dia 4 — Playwright: instalação e primeiros conceitos

### Instalação

```bash
pip install pytest
pip install playwright
pip install pytest-playwright
playwright install          # baixa os browsers
```

**Verificar:**
```bash
playwright --version        # Version 1.60.0
pytest --version            # pytest 9.0.3
```

---

### Os 4 conceitos fundamentais

| Conceito | Analogia | O que é |
|---|---|---|
| Browser | A cidade | Instância do browser (Chromium, Firefox, WebKit) |
| BrowserContext | Escritório isolado | Ambiente sem cookies cruzados entre testes |
| Page | A cena do crime | A página onde você interage |
| Locator | A lupa | Forma semântica de encontrar elementos |

---

### Locators — do mais para o menos recomendado

```python
# ✅ Recomendados — semânticos e robustos
page.get_by_role("button", name="Entrar")
page.get_by_label("Email")
page.get_by_placeholder("Digite seu email")
page.get_by_text("Bem-vindo")
page.get_by_test_id("submit-btn")

# ⚠️ Evitar — frágeis, quebram com mudança de layout
page.locator("//div/span/button")        # XPath
page.locator(".btn-primary > span")      # CSS genérico
```

---

### Padrão AAA — estrutura universal de teste

```python
def test_transferencia_pix(page: Page):

    # Arrange — preparar a cena
    page.goto("https://app.banco.com/pix")

    # Act — executar a ação
    page.get_by_label("Chave PIX").fill("email@destino.com")
    page.get_by_label("Valor").fill("100")
    page.get_by_role("button", name="Confirmar").click()

    # Assert — validar o resultado
    expect(page.get_by_text("Transferência realizada")).to_be_visible()
```

---

### Assertions mais usadas

```python
from playwright.sync_api import expect

expect(page).to_have_title("Nubank")
expect(page).to_have_url("https://nubank.com.br/home")
expect(page).not_to_have_url("https://nubank.com.br/")

expect(page.get_by_text("Bem-vindo")).to_be_visible()
expect(page.get_by_role("heading")).to_have_text("Resultados")
expect(page.get_by_role("button", name="Enviar")).to_be_enabled()
expect(page.get_by_label("Email")).to_have_value("teste@email.com")
```

---

### Como rodar os testes

```bash
pytest                              # headless, todos os testes
pytest -v                           # com detalhes no terminal
pytest --headed                     # abre o browser visualmente
pytest --headed --slowmo=1000       # abre o browser em câmera lenta
pytest test_arquivo.py              # arquivo específico
pytest -k "nome_do_teste"           # teste específico pelo nome
```

---

### Headed vs Headless

| Modo | Quando usar |
|---|---|
| `--headed` | Debug, aprendizado, ver o que está acontecendo |
| headless (padrão) | CI/CD, execução rápida, produção |

---

### Erros comuns no Playwright e como resolver

| Erro | Causa | Solução |
|---|---|---|
| `AttributeError: get_by_name` | Método não existe no Python | Usar `get_by_placeholder` ou `get_by_label` |
| `TimeoutError: 30000ms exceeded` | Elemento não encontrado | Verificar o locator correto com DevTools (F12) |
| Browser não abre | Browsers não instalados | Rodar `playwright install` |
| Site bloqueia headless | Anti-bot do site | Usar `--headed` ou trocar para site de prática |

---

### Resumo Dia 4

| Conceito | Em uma frase |
|---|---|
| Browser | Instância do browser controlada pelo Playwright |
| BrowserContext | Ambiente isolado — sem cookies entre testes |
| Page | A página onde você interage |
| Locator | Forma semântica de encontrar elementos |
| AAA | Arrange, Act, Assert — estrutura universal |
| `expect()` | Forma de validar resultados |
| `--headed` | Roda com browser visível — ideal para debug |

---

## Exercícios realizados

### Dia 1 — Pirâmide de testes (app de banco)

**Exercício:** Classificar 8 situações como Unitário, Integração ou E2E.

**Regra que você criou (melhor que qualquer definição de livro):**
- Unitário = não precisa de ninguém para ser validado
- Integração = precisa de outro(s) para funcionar
- E2E = fluxo que o cliente faria

**Gabarito:**

| Situação | Camada | Por quê |
|---|---|---|
| Função de juros 2% ao mês | Unitário | Lógica isolada, sem dependência |
| Login → extrato → exportar PDF | E2E | Fluxo completo do usuário |
| Notificação após transferência aprovada | Integração | Módulo de notificação + serviço de push |
| Função valida CPF "000.000.000-00" | Unitário | Validação isolada |
| App exibe erro quando servidor retorna 500 | Integração | App dependendo de servidor externo |
| Cadastro → confirmar email → primeiro login | E2E* | Fluxo completo (*email é nuance de escopo) |
| Função formata data "2026-05-15" → "15/05/2026" | Unitário | Formatação pura, sem dependência |
| Banco salva dados após pagamento aprovar | Integração | Serviço de pagamento + banco de dados |

---

### Dia 2 — Casos de teste do fluxo PIX (Nubank)

**Exercício:** Escrever 6 casos de teste (2 happy path, 2 negativos, 2 borda) + 1 bug report.

**Casos escritos:**

| ID | Cenário | Tipo | Status |
|---|---|---|---|
| TC-PIX-03 | Email sem @ aceito no cadastro | Negativo | FAIL — bug encontrado |
| TC-PIX-04 | App fecha após transferência confirmada | Happy path | FAIL — bug crítico |
| TC-PIX-05 | Transferência acima de R$ 5.000 processada | Borda (máximo) | FAIL — bug alto |
| TC-PIX-06 | Transferência de R$ 0,00 processada | Borda (mínimo) | FAIL — bug alto |

**Aprendizados da correção:**
- Pré-condição = estado do sistema, NÃO é passo
- Título de bug = o quê + onde + condição
- Casos de borda vêm em pares: mínimo E máximo
- App fechando em operação financeira = Severidade Crítico, não Alto

---

### Dia 3 — Repositório qa-portfolio no GitHub

**Exercício:** Criar repositório, estruturar pastas, commitar casos de teste.

**Resultado:**
- Repositório criado: github.com/Barbosavanderson/qa-portfolio
- Estrutura: `casos-de-teste/` · `bugs/` · `projetos/`
- Commits: feat + docs separados por tipo
- README profissional com roadmap das 8 semanas

**Erro encontrado e resolvido:**
```bash
# Problema: master vs main — conflito de branches
# Solução:
git branch -m master main
git push origin main --force
```

---

### Dia 4 — Primeiro teste com Playwright

**Exercício:** Escrever teste que abre DuckDuckGo e valida resultado de busca.

**Erro encontrado:**
```
AttributeError: 'Page' object has no attribute 'get_by_name'
```

**Aprendizado:** `get_by_name` é JavaScript. Em Python usar `get_by_placeholder`.

**Código final funcionando:**
```python
from playwright.sync_api import Page, expect

def test_busca_retorna_resultados(page: Page):
    # Arrange
    page.goto("https://duckduckgo.com")

    # Act
    page.get_by_placeholder("Search the web").fill("Vanderson Barbosa QA")
    page.get_by_placeholder("Search the web").press("Enter")

    # Assert
    expect(page).not_to_have_url("https://duckduckgo.com/")
```

**Nota registrada:** DuckDuckGo bloqueia acesso headless com timeout.
Solução: usar `--headed` ou trocar para site sem anti-bot.
Conceito validado: goto, get_by_placeholder, fill, press, expect.

---

## Erros comuns e como resolver

### Git

```bash
# Conflito master vs main
git branch -m master main
git push origin main --force

# Nada para commitar mas tenho arquivos novos
git add .
git commit -m "feat: ..."

# Push rejeitado
git pull origin main --allow-unrelated-histories
git push origin main
```

### Playwright

```python
# Erro: get_by_name não existe em Python
# ❌ page.get_by_name("q").fill("texto")
# ✅ page.get_by_placeholder("Search").fill("texto")

# Erro: TimeoutError — elemento não encontrado
# Abrir o browser com F12 e inspecionar o elemento real
# Verificar o placeholder, label ou role correto

# Site bloqueia headless
# Usar --headed na execução
# pytest test_arquivo.py --headed -v
```

---

*Material em construção — atualizado a cada dia de estudo.*  
*Vanderson Barbosa · QA Portfolio 2026*
