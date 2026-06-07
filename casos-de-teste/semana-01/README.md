# Matriz de Risco — App Bancário
**Semana 01 · Dia 05 — Risk-based Testing**

---

## Conceito

Risk-based Testing é a estratégia de priorizar testes com base no **risco** de cada funcionalidade.

Risco = **Impacto** × **Probabilidade**

- **Impacto**: o estrago causado se a funcionalidade falhar
- **Probabilidade**: a chance real de aquilo falhar (baseada em complexidade, histórico e frequência de mudança)

Quando o tempo é limitado, testamos primeiro o que tem **maior risco** — não o que é mais fácil.

---

## Quadrantes da Matriz 3×3

```
                    IMPACTO
                Baixo   Médio   Alto
              ┌───────┬───────┬───────┐
         Alta │   M   │   H   │ CRIT  │
              ├───────┼───────┼───────┤
Prob.   Média │   L   │   M   │  HIGH │
              ├───────┼───────┼───────┤
        Baixa │   L   │   L   │   M   │
              └───────┴───────┴───────┘
```

| Sigla | Significado | Ação |
|-------|-------------|------|
| CRIT  | Crítico     | Testa primeiro, sempre, com cobertura máxima |
| HIGH  | Alto        | Testa logo após os críticos, boa cobertura |
| M     | Médio       | Testa se houver tempo, cobertura básica |
| L     | Baixo       | Testa por último ou omite se tempo acabar |

---

## Matriz — Funcionalidades do App Bancário

| Funcionalidade     | Impacto | Probabilidade | Quadrante | Justificativa |
|--------------------|---------|---------------|-----------|---------------|
| Login              | Alto    | Médio         | HIGH      | Sem login nenhuma função é acessível; fluxo estável mas com múltiplos vetores de falha (timeout, credencial, sessão) |
| Transferência PIX  | Alto    | Alto          | CRIT      | Movimentação financeira real; alta complexidade e integração com Banco Central; bug = prejuízo imediato |
| Extrato            | Alto    | Médio         | HIGH      | Valor errado no extrato = cliente não detecta cobrança indevida; impacto financeiro e legal alto |
| Alteração de senha | Alto    | Médio         | HIGH      | Senha comprometida = conta invadida; fluxo simples reduz probabilidade, mas impacto é alto |
| Tema escuro/claro  | Baixo   | Médio         | LOW       | Puramente cosmético; não afeta nenhuma regra de negócio nem dado financeiro |
| Cadastro chave PIX | Alto    | Médio         | HIGH      | Chave errada = PIX enviado para destinatário errado; menos complexo que a transferência em si |

---

## Ordem de Execução dos Testes

Com base no risco, a ordem de execução é:

1. **Transferência PIX** — CRIT, maior risco absoluto
2. **Login** — HIGH, pré-requisito para tudo
3. **Extrato** — HIGH, impacto financeiro/legal silencioso
4. **Alteração de senha** — HIGH, impacto de segurança
5. **Cadastro de chave PIX** — HIGH, pré-requisito para o PIX
6. **Tema escuro/claro** — LOW, testado somente se sobrar tempo

---

## Conceitos-chave do Dia

**Test Coverage** — percentual do sistema coberto por testes. 100% é impossível na prática porque o número de combinações de entrada é infinito. O objetivo é cobrir os caminhos de **maior risco** primeiro.

**Risco de Produto** — o software tem defeito que prejudica o usuário (ex: bug no PIX).

**Risco de Projeto** — o processo de desenvolvimento falha (ex: requisito mal levantado, prazo estourado).

---

## Aprendizados do Dia

- Risco não é intuição — é cruzamento sistemático de impacto × probabilidade
- Impacto alto nunca é ignorado, mesmo com probabilidade baixa
- Probabilidade se estima por complexidade técnica, histórico de bugs e frequência de mudança
- Testar igualmente tudo é desperdício — Risk-based Testing é a saída profissional

---

*Semana 01 · Dia 05 | Plano QA 8 Semanas*
