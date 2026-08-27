Problema

O sistema negava crédito a quem não comprovasse renda formal (CLT), rejeitando 95% das mulheres chefes de família da comunidade, mesmo com ótimo histórico de pagamento.
A renda era verificada dentro da aprovação pelo score, funcionando como filtro excludente: score 100 com renda zero dava "Reprovado".
A correção usa um Score Social Alternativo, baseado no comportamento observável do cliente (contas em dia, fluxo de caixa do negócio, tempo de ponto, grupo solidário e referências locais).

1) Entrada: score social  
Lê o score de 0 a 100 num laço while, que só avança com valor válido.
O try/except ValueError trata texto digitado por engano. O except é específico porque um genérico engoliria o Ctrl+C.

2) Entrada: renda formal CLT  
Mesma validação, aceitando apenas valores não negativos.
Quem é informal digita 0 e segue na análise: a renda é coletada, mas não barra ninguém.

3) Bônus de renda  
A renda vira um bônus que soma pontos, com teto de 15 e saturação em R$ 3.000.
Média ponderada (70% social + 30% renda) seria injusta: o zero do informal entraria na média e viraria punição, limitando seu teto a 70 pontos.
Com a soma, renda zero é ausência de bônus, não penalidade. E como 15 é menor que o limiar de 60, a renda nunca aprova sozinha.

4) Decisão  
A análise começa sempre pelo score social, em if / elif / else.
Score 60 ou mais aprova direto, sem consultar a renda. De 45 a 59, o bônus pode completar a nota. Abaixo de 45, reprovado.
A saída exibe Resultado: Aprovado ou Resultado: Reprovado com o motivo.
Na prática: score 70 sem carteira passou de reprovado a aprovado; score 43 com R$ 3.000 passou de aprovado a reprovado.
