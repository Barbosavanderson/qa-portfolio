# Casos de Teste — Transferência PIX
**Sistema:** Nubank App  
**Versão:** 17.04  
**Autor:** Anderson Barbosa  
**Data:** 18/05/2026  

---

## TC-PIX-03 — Validação de email sem @ no cadastro

**Pré-condição:** Usuário na tela de cadastro do Nubank  
**Passos:**  
1. Acessar tela de cadastro
2. Digitar email sem o caractere @ no campo Email
3. Avançar para o próximo campo  

**Resultado esperado:** Sistema exibe mensagem solicitando verificar o formato do email  
**Resultado obtido:** Sistema aceita e avança para o próximo campo sem validar  
**Status:** FAIL  
**Severidade:** Alta  
**Prioridade:** Alta  

---

## TC-PIX-04 — App fecha após transferência confirmada

**Pré-condição:** Usuário logado, saldo R$ 500,00, chave PIX destino válida  
**Passos:**  
1. Acessar tela de transferência PIX
2. Digitar chave PIX válida no campo destino
3. Digitar R$ 100,00 no campo valor
4. Tocar em Confirmar transferência
5. Inserir senha de 4 dígitos correta
6. Tocar em Confirmar  

**Resultado esperado:** Tela de comprovante exibida com valor, destinatário e botão salvar PDF  
**Resultado obtido:** App fecha e retorna para tela inicial do smartphone sem exibir comprovante  
**Status:** FAIL  
**Severidade:** Crítico  
**Prioridade:** Alta  

---

## TC-PIX-05 — Transferência acima do limite de R$ 5.000,00

**Pré-condição:** Usuário logado, saldo R$ 6.000,00, chave PIX destino válida  
**Passos:**  
1. Acessar tela de transferência PIX
2. Digitar chave PIX válida
3. Digitar R$ 5.000,01 no campo valor
4. Tocar em Confirmar transferência
5. Inserir senha correta
6. Tocar em Confirmar  

**Resultado esperado:** Sistema bloqueia e exibe "Valor acima do limite de R$ 5.000,00 por transação"  
**Resultado obtido:** Transferência processada normalmente, comprovante exibido com R$ 5.000,01  
**Status:** FAIL  
**Severidade:** Alta  
**Prioridade:** Alta  

---

## TC-PIX-06 — Transferência abaixo do valor mínimo de R$ 0,01

**Pré-condição:** Usuário logado, saldo R$ 100,00, chave PIX destino válida  
**Passos:**  
1. Acessar tela de transferência PIX
2. Digitar chave PIX válida
3. Digitar R$ 0,00 no campo valor
4. Tocar em Confirmar transferência
5. Inserir senha correta
6. Tocar em Confirmar  

**Resultado esperado:** Sistema bloqueia e exibe "Valor mínimo de transação é R$ 0,01"  
**Resultado obtido:** Transferência processada, comprovante exibido com valor R$ 0,00  
**Status:** FAIL  
**Severidade:** Alta  
**Prioridade:** Alta