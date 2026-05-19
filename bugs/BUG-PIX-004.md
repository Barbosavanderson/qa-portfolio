# BUG-PIX-004 — App fecha após confirmação de transferência PIX

**ID:** BUG-PIX-004  
**Data:** 18/05/2026  
**Autor:** Anderson Barbosa  

---

## Identificação

| Campo       | Valor                          |
|-------------|-------------------------------|
| Severidade  | Crítico                        |
| Prioridade  | Alta                           |
| Status      | Aberto                         |
| Ambiente    | Android 12.1 · Nubank App v17.3 · Homologação |

---

## Título

App fecha inesperadamente após confirmação de transferência PIX no Android 12.1

---

## Pré-condição

- Usuário logado na conta Nubank  
- Saldo disponível de R$ 500,00  
- Chave PIX destino válida cadastrada  
- Ambiente de homologação ativo  

---

## Passos para reproduzir

1. Acessar a tela de transferência PIX  
2. Digitar chave PIX válida no campo destino  
3. Digitar R$ 100,00 no campo valor  
4. Tocar em **Confirmar transferência**  
5. Inserir senha de 4 dígitos correta  
6. Tocar em **Confirmar**  

---

## Resultado esperado

Tela de comprovante exibida contendo:
- Valor transferido
- Nome e chave do destinatário
- Data e hora da transação
- Botão para salvar comprovante em PDF

---

## Resultado obtido

App fecha imediatamente após o toque em **Confirmar** e retorna para a tela inicial do smartphone.  
Nenhum comprovante é exibido. Usuário não consegue confirmar se a transferência foi realizada.

---

## Evidência

> Screenshot e gravação de tela mostrando o app fechando logo após a confirmação.  
> Tela inicial do smartphone exibida em seguida, sem nenhuma notificação do app.

---

## Impacto

Usuário fica sem comprovante de operação financeira realizada.  
Risco de dupla cobrança por re-tentativa. Possível impacto jurídico e de suporte.  
**Release deve ser bloqueado até correção.**