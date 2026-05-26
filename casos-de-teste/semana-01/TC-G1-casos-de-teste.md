# Casos de Teste e Matriz de Risco — Auditoria G1 News
**Projeto:** Semana 01 — Auditor do G1 News  
**Sistema:** Portal G1 (g1.globo.com)  
**Autor:** Vanderson Barbosa  
**Data:** 24/05/2026  

---

## Índice
1. [Casos de Teste](#casos-de-teste)
2. [Matriz de Risco](#matriz-de-risco)
3. [Resumo de Bugs Encontrados](#resumo-de-bugs-encontrados)

---

## Casos de Teste

---

### TC-G1-001 — Navegação: acesso ao link O Globo

| Campo | Detalhe |
|---|---|
| **ID** | TC-G1-001 |
| **Tipo** | Navegação |
| **Status** | ✅ PASS |

**Descrição:** Verificar se o link do jornal O Globo na barra superior redireciona corretamente.

**Pré-condição:** Usuário na página principal do G1 (https://g1.globo.com/)

**Passos:**
1. Acessar a página principal do G1 (https://g1.globo.com/)
2. Localizar o link "O Globo" na barra superior de navegação
3. Clicar no link

**Resultado esperado:** Usuário redirecionado para (https://oglobo.globo.com/)

**Resultado obtido:** Usuário redirecionado corretamente para (https://oglobo.globo.com/)

---

### TC-G1-002 — Navegação: acesso ao "Anuncie conosco" no footer

| Campo | Detalhe |
|---|---|
| **ID** | TC-G1-002 |
| **Tipo** | Navegação |
| **Status** | ✅ PASS |

**Descrição:** Verificar se o link "Anuncie conosco" no footer redireciona para a página correta.

**Pré-condição:** Usuário na página principal do G1 (https://g1.globo.com/)

**Passos:**
1. Acessar a página principal do G1
2. Rolar até o footer da página
3. Localizar e clicar em "Anuncie conosco"

**Resultado esperado:** Usuário redirecionado para (https://globoads.globo.com/)

**Resultado obtido:** Usuário redirecionado corretamente para (https://globoads.globo.com/)

---

### TC-G1-003 — Busca: pesquisa por palavra-chave retorna resultados

| Campo | Detalhe |
|---|---|
| **ID** | TC-G1-003 |
| **Tipo** | Funcional — Busca |
| **Status** | ✅ PASS |

**Descrição:** Verificar se a busca retorna notícias relacionadas ao termo pesquisado.

**Pré-condição:** Usuário na página principal do G1

**Passos:**
1. Acessar a página principal do G1
2. Localizar o ícone de lupa (busca)
3. Digitar "Playwright" no campo de busca
4. Confirmar a busca

**Resultado esperado:** Página de resultados exibe notícias contendo a palavra "Playwright" ou termos relacionados

**Resultado obtido:** Matérias com a palavra-chave retornaram corretamente. Sistema também exibe resultados com termos parecidos — comportamento esperado para auxiliar buscas com erro de digitação.

---

### TC-G1-004 — Banner patrocinado: redirecionamento ao clicar

| Campo | Detalhe |
|---|---|
| **ID** | TC-G1-004 |
| **Tipo** | Funcional — Publicidade |
| **Status** | ❌ FAIL |
| **Severidade** | Alta |
| **Prioridade** | Alta |

**Descrição:** Verificar se o clique em banner patrocinado redireciona para a página correta do anunciante.

**Pré-condição:** Banner JBL visível na home do G1 em 24/05/2026 às 14h

**Passos:**
1. Acessar a página principal do G1
2. Localizar o banner patrocinado "JBL" na home
3. Clicar no banner
4. Aguardar redirecionamento

**Resultado esperado:** Usuário redirecionado para o site da JBL (https://www.jbl.com.br/)

**Resultado obtido:** Erro 404 — link da página incorreto. Usuário não é redirecionado para o destino do anunciante.

**Evidência:** Screenshot da página de erro 404 após clique no banner JBL

**Impacto:** Anunciante pagou pelo espaço e o link está quebrado — perda de receita direta e experiência negativa para o usuário.

---

### TC-G1-005 — Login: acesso com dados válidos via conta Globo

| Campo | Detalhe |
|---|---|
| **ID** | TC-G1-005 |
| **Tipo** | Funcional — Autenticação |
| **Status** | ❌ FAIL |
| **Severidade** | Crítico |
| **Prioridade** | Crítica |

**Descrição:** Verificar se o fluxo de login com credenciais válidas segue todas as etapas corretamente.

**Pré-condição:** Usuário com conta Globo cadastrada e ativa

**Passos:**
1. Acessar a página principal do G1
2. Localizar o botão "Entrar" no canto superior direito
3. Clicar em "Entrar" no pop-up exibido
4. Inserir e-mail válido: `usuario_teste@exemplo.com`
5. Inserir senha válida: `********`
6. Confirmar o login

**Resultado esperado:** Após inserir e-mail e senha, usuário é direcionado para a tela de perfil

**Resultado obtido:** Após inserir apenas o e-mail, usuário é redirecionado diretamente para a tela de perfil sem solicitar a senha — etapa de autenticação por senha ignorada pelo sistema.

**Evidência:** Gravação de tela mostrando o fluxo pulando a etapa de senha

**Impacto:** Falha crítica de segurança — qualquer pessoa com o e-mail de um usuário consegue acessar a conta sem conhecer a senha.

---

## Matriz de Risco

> **Fórmula:** Prioridade de teste = Impacto × Probabilidade de falha  
> **Impacto:** 1 = baixo · 2 = médio · 3 = alto  
> **Probabilidade:** 1 = raramente falha · 2 = às vezes · 3 = falha com frequência

| Funcionalidade | Impacto (1-3) | Probabilidade (1-3) | Prioridade | Quando testar |
|---|---|---|---|---|
| Login conta Globo | 3 | 3 | **9** | Sempre — todo ciclo |
| Links do footer | 2 | 3 | **6** | Todo release |
| Banners patrocinados | 3 | 2 | **6** | Todo release |
| Navegação header (O Globo) | 2 | 2 | **4** | Releases importantes |
| Busca de notícias | 2 | 1 | **2** | Quando houver tempo |

### Ordem de execução dos testes baseada no risco

```
1º Login conta Globo      → prioridade 9  → testa SEMPRE primeiro
2º Links do footer        → prioridade 6  → testa em todo release
3º Banners patrocinados   → prioridade 6  → testa em todo release
4º Navegação header       → prioridade 4  → testa em releases importantes
5º Busca de notícias      → prioridade 2  → testa quando houver tempo
```

---

## Resumo de Bugs Encontrados

| ID | Título | Severidade | Prioridade | Status |
|---|---|---|---|---|
| BUG-G1-001 | Banner JBL retorna erro 404 ao clicar na home do G1 | Alta | Alta | Aberto |
| BUG-G1-002 | Login ignora etapa de senha e autentica só com e-mail | Crítico | Crítica | Aberto |

---

## Lições aprendidas

- Banners patrocinados são dinâmicos — sempre registrar data e horário na pré-condição
- Bugs de autenticação têm impacto de segurança — severidade Crítico independente do fluxo parecer funcionar
- Casos de sucesso não recebem severidade/prioridade — esses campos são exclusivos de bugs
- Credenciais nunca devem ser documentadas em texto claro — usar `********` para senhas

---

*Vanderson Barbosa · QA Portfolio 2026 · Semana 01 — Auditor do G1 News*
