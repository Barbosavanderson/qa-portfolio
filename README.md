# 🧪 QA Portfolio — Anderson Barbosa

> Repositório de estudos e projetos práticos de **Quality Engineering moderno**.  
> Baseado em análise de vagas reais do mercado brasileiro (2026) e revisado por QA Sênior.

---

## 👤 Sobre

Transição de carreira para Quality Engineering com foco em automação, testes de API e boas práticas modernas.  
Este repositório documenta a jornada completa — da teoria aos projetos reais em sistemas públicos.

**Stack em construção:**  
`Playwright` · `Python` · `Postman` · `SQL` · `Git` · `Jira` · `GitHub Actions` · `k6` · `IA aplicada a QA`

---

## 🗺️ Roadmap — 8 semanas de treinamento

| Semana | Fase | Foco principal | Projeto |
|--------|------|---------------|---------|
| 01 | Fundamentos QA | Teoria, casos de teste, bugs, Git | [Auditor do G1 News](#-semana-01--auditor-do-g1-news) |
| 02 | Fundamentos QA | User stories, Jira, Shift Left | [Risk Map PIX](#-semana-02--risk-map-pix) |
| 🔵 | **Checkpoint 1** | Consolidação semanas 1 e 2 | Revisão geral |
| 03 | Automação | Playwright, POM, fixtures | [iFood QA Suite](#-semana-03--ifood-qa-suite) |
| 04 | Automação | CI/CD, flaky tests, chaos | [Chaos Tester](#-semana-04--chaos-tester) |
| 🔵 | **Checkpoint 2** | Consolidação semanas 3 e 4 | Revisão geral |
| 05 | APIs e dados | Postman, REST, contratos | [API Watchdog](#-semana-05--api-watchdog) |
| 06 | APIs e dados | SQL, integridade, API x banco | [Data Detective](#-semana-06--data-detective) |
| 🔵 | **Checkpoint 3** | Consolidação semanas 5 e 6 | Revisão geral |
| 07 | Quality Engineering | Observabilidade, performance, IA | [AI QA Copilot](#-semana-07--ai-qa-copilot) |
| 08 | Portfólio | GitHub, LinkedIn, storytelling | [QA Guardian](#-semana-08--qa-guardian-projeto-integrador) |

---

## 📁 Estrutura do repositório

```
qa-portfolio/
├── README.md                        ← você está aqui
├── docs/
│   └── roadmap-semanal.md           ← mapa detalhado semana a semana
├── casos-de-teste/
│   ├── semana-01/                   ← casos escritos antes de qualquer automação
│   ├── semana-02/
│   └── .../
├── bugs/
│   └── BUG-PIX-004.md               ← bugs reportados com todos os campos
├── projetos/
│   ├── semana-01-auditor-g1/        ← projeto completo com README próprio
│   ├── semana-02-risk-map-pix/
│   ├── semana-03-ifood-qa-suite/
│   ├── semana-04-chaos-tester/
│   ├── semana-05-api-watchdog/
│   ├── semana-06-data-detective/
│   ├── semana-07-ai-qa-copilot/
│   └── semana-08-qa-guardian/
└── .github/
    └── workflows/
        └── tests.yml                ← CI/CD GitHub Actions (a partir semana 4)
```

---

## 🚀 Projetos

### 📰 Semana 01 — Auditor do G1 News
> **Status:** ✅ Concluído

Auditoria de qualidade no portal G1 (g1.globo.com) — sistema real com milhões de usuários diários.

**O que foi feito:**
- 10 casos de teste documentados antes de qualquer automação
- Matriz de risco das funcionalidades testadas
- Bugs reportados com todos os campos profissionais

**Habilidades praticadas:** `casos de teste` `report de bugs` `matriz de risco` `Git`

📂 [Ver projeto](./projetos/semana-01-auditor-g1/)

---

### 💰 Semana 02 — Risk Map PIX
> **Status:** 🔄 Em andamento

Estratégia completa de testes para um sistema fictício de pagamento PIX — criando requisitos do zero e testando em cima deles.

**O que será feito:**
- Documento de requisitos com 5 user stories e critérios de aceite
- Perguntas Shift Left para o time de desenvolvimento
- Matriz de risco completa
- 15 casos de teste cobrindo fluxos felizes, negativos, borda e segurança

**Habilidades praticadas:** `user stories` `critérios de aceite` `Jira` `Shift Left` `estratégia de testes`

📂 [Ver projeto](./projetos/semana-02-risk-map-pix/)

---

### 🛒 Semana 03 — iFood QA Suite
> **Status:** ⏳ Aguardando

Suíte E2E automatizada com Playwright no iFood — e-commerce real com estado de UI dinâmico.

**O que será feito:**
- Page Object Model com classes por página
- Fixtures reutilizáveis no pytest
- Screenshots automáticos em falhas
- CI/CD no GitHub Actions

**Habilidades praticadas:** `Playwright` `POM` `pytest` `fixtures` `CI/CD`

📂 [Ver projeto](./projetos/semana-03-ifood-qa-suite/)

---

### 💥 Semana 04 — Chaos Tester
> **Status:** ⏳ Aguardando

Engenharia do caos aplicada a QA — interceptação de APIs, mocks de erro e diagnóstico de flaky tests.

**O que será feito:**
- Mock de respostas de API com erros 500, timeout e payload inválido
- Testes de borda extremos: SQL injection, emoji, 500 caracteres
- Diagnóstico e correção de flaky tests com Playwright Trace Viewer
- Execução paralela com pytest-xdist

**Habilidades praticadas:** `chaos testing` `mock de API` `flaky tests` `paralelismo`

📂 [Ver projeto](./projetos/semana-04-chaos-tester/)

---

### 🌦️ Semana 05 — API Watchdog
> **Status:** ⏳ Aguardando

Monitor de qualidade da API do OpenWeather — validando consistência entre API e UI.

**O que será feito:**
- Collection Postman com 8 testes automatizados
- Validação de contrato JSON Schema
- Testes de tempo de resposta (< 2s)
- Consistência API x UI com Playwright

**Habilidades praticadas:** `Postman` `REST` `contrato de API` `JSON Schema` `API x UI`

📂 [Ver projeto](./projetos/semana-05-api-watchdog/)

---

### 🕵️ Semana 06 — Data Detective
> **Status:** ⏳ Aguardando

Investigação forense no Portal da Transparência — cruzando dados entre API e SQL.

**O que será feito:**
- 10 queries SQL validando integridade dos dados da API
- Suíte Playwright nos endpoints públicos do governo
- Relatório de anomalias documentado como bugs no Jira
- Script de geração de massa de dados

**Habilidades praticadas:** `SQL` `JOIN` `GROUP BY` `API pública` `integridade de dados`

📂 [Ver projeto](./projetos/semana-06-data-detective/)

---

### 🤖 Semana 07 — AI QA Copilot
> **Status:** ⏳ Aguardando

Workflow documentado de uso de IA no processo de QA — com prompt library testada e refinada.

**O que será feito:**
- 10 prompts para geração de casos de teste, massa de dados e análise de logs
- Script k6 de performance em API pública
- Checklist de segurança básica (OWASP Top 10)
- Documentação de casos onde a IA errou e como detectar

**Habilidades praticadas:** `IA aplicada a QA` `prompt engineering` `k6` `observabilidade` `segurança`

📂 [Ver projeto](./projetos/semana-07-ai-qa-copilot/)

---

### 🛡️ Semana 08 — QA Guardian (Projeto integrador)
> **Status:** ⏳ Aguardando

Projeto integrador que reúne todas as camadas técnicas em um único repositório de nível sênior.

**O que será feito:**
- Suíte Playwright E2E + API + SQL integrados
- CI/CD rodando Playwright e Postman via Newman
- Relatório HTML consolidado com evidências
- README de nível sênior com decisões técnicas e lições aprendidas

**Habilidades praticadas:** `integração completa` `Newman` `CI/CD` `portfólio` `storytelling técnico`

📂 [Ver projeto](./projetos/semana-08-qa-guardian/)

---

## 🛠️ Tecnologias utilizadas

| Ferramenta | Categoria | A partir de |
|------------|-----------|-------------|
| Git / GitHub | Versionamento | Semana 1 |
| Markdown | Documentação | Semana 1 |
| Jira | Gestão de bugs | Semana 2 |
| Playwright + Python | Automação E2E | Semana 3 |
| pytest | Framework de testes | Semana 3 |
| GitHub Actions | CI/CD | Semana 4 |
| Postman | API Testing | Semana 5 |
| SQL | Validação de dados | Semana 6 |
| k6 | Performance testing | Semana 7 |
| Claude / ChatGPT | IA aplicada a QA | Semana 7 |

---

## 📊 Progresso atual

- [x] Semana 01 — Fundamentos QA e Git
- [ ] Semana 02 — User Stories e Jira
- [ ] Semana 03 — Playwright
- [ ] Semana 04 — CI/CD e Chaos Testing
- [ ] Semana 05 — API Testing
- [ ] Semana 06 — SQL e dados
- [ ] Semana 07 — Quality Engineering + IA
- [ ] Semana 08 — Portfólio final

---

## 📬 Contato

**Anderson Barbosa**  
🔗 [LinkedIn](https://linkedin.com/in/seu-perfil) ← atualize com seu link  
📧 seu-email@gmail.com ← atualize com seu email  
🐙 [github.com/Barbosavanderson](https://github.com/Barbosavanderson)

---

> *"Um QA que não documenta é um QA que não existiu."*  
> — Princípio do Quality Engineering moderno
