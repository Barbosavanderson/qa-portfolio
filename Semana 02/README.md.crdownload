# User Stories e Critérios de Aceite
**Semana 02 · Dia 01 — QA na leitura de histórias de usuário**

---

## Conceito

Uma **User Story** descreve uma funcionalidade do ponto de vista do usuário:

> Como [ator], eu quero [ação], para que [benefício]

Ela é proposital e curta — não é especificação técnica. O detalhe entra através dos **Critérios de Aceite**: a lista de condições que define quando a história está "pronta" e funcionando como esperado.

**Erro comum de QA júnior:** tratar o critério de aceite como uma ferramenta de conferência pós-implementação ("o dev terminou, agora eu checo"). Isso é tarde. O critério de aceite é uma ferramenta de **antes** — usada no refinamento, junto com PO e dev, para encontrar lacunas antes que qualquer linha de código seja escrita.

---

## Por que critério de aceite só com cenário positivo é um risco

Um critério como:

> "O cliente consegue fazer login com credenciais válidas."

cobre o caminho feliz e nada mais. O que ele NÃO responde:

- O que acontece com credenciais inválidas? Qual mensagem aparece?
- Quantas tentativas até a conta travar?
- Campo vazio é bloqueado no envio?
- A senha aparece mascarada?
- Existe expiração de sessão?
- O sistema trata caracteres especiais / tentativa de injeção?

Cada pergunta sem resposta é um cenário que **não vai ser testado** porque ninguém pensou nele a tempo — e vai aparecer como bug em produção, gerando confusão pro usuário (ex: tela de login que não mostra erro nenhum com dados errados).

---

## Ação concreta do QA no refinamento

Não é "pensar com cuidado". É:

1. Ler a história e o critério de aceite propostos.
2. Levantar em voz alta, na reunião, os cenários negativos/bordas que faltam.
3. Propor que cada resposta vire um **novo critério de aceite escrito** — não fica só falado na sala.

Isso é a aplicação prática de **shift-left**: testar (ou pelo menos pensar em teste) o mais cedo possível no ciclo, porque um gap pego no refinamento nunca chega a virar código errado — e código errado é o que custa caro de corrigir.

---

## Critério de aceite ambíguo → testável (exemplo trabalhado)

**Ambíguo:**
> "Cliente pode escolher o tipo de verificação para o acesso."

Problema: não diz quais são as opções, nem se é uma escolha única ou múltipla.

**Primeira tentativa de correção (ainda com problema):**
> "Cliente deve cadastrar os tipos de verificação sendo eles: senha, confirmação de 2 fatores e leitura de QR code."

Problema: trocou "escolher" por "cadastrar" — agora não está claro se o cliente é obrigado a configurar os três métodos ou só um.

**Versão testável final:**
> "Cliente deve escolher **uma** entre as opções de verificação: senha, confirmação de 2 fatores ou leitura de QR code."

Agora dá pra montar casos de teste objetivos:
- Login com senha → sucesso
- Login com 2FA → sucesso
- Login com QR code → sucesso
- Tentativa sem selecionar nenhum método → comportamento esperado?

---

## Cenário de Teste x Caso de Teste

| | Cenário de Teste | Caso de Teste |
|---|---|---|
| Nível | Alto, descreve "o quê" testar | Detalhado, descreve "como" testar |
| Exemplo | "Verificar login com diferentes métodos de verificação" | Passos: 1) Abrir app 2) Selecionar "senha" 3) Inserir senha correta 4) Esperado: redireciona pra home |
| Relação | Agrupa múltiplos casos de teste | É a unidade mínima, com entrada/saída específica |

---

## Contra-argumento pro PO que diz "não precisa de critério de aceite, a história já está clara"

Clareza na sala não é clareza documentada. O entendimento comum entre quem está na reunião não se transmite automaticamente pra quem entra no time depois, pra outro QA que vai regressionar isso em 3 meses, ou pra auditoria. Escrever o critério custa minutos agora; reconstruir o entendimento (ou corrigir um bug de interpretação errada) custa muito mais depois.

---

## Aprendizados do Dia

- Critério de aceite é ferramenta de **antes**, não só de checagem pós-implementação
- Todo critério escrito só com caminho feliz esconde cenários negativos não testados
- Mudar uma palavra ("escolher" → "cadastrar") pode reintroduzir ambiguidade — releia sempre com olhar de quem vai testar
- Cenário de teste agrupa casos de teste; caso de teste é a unidade detalhada de entrada/saída
- Shift-left = pegar gap no refinamento = nunca vira bug de código = menos retrabalho e custo

---

*Semana 02 · Dia 01 | Plano QA 8 Semanas*
