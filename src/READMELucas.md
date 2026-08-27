# Sistema de Score de Microcrédito Inclusivo

Trabalho da disciplina de Sistemas de Informação - UniFAP
Arquivo do sistema: `src/triagem.py` (roda em Python 3, não precisa instalar nada)

O programa foi feito só com `if` e `else` (sem funções), pra ficar mais
simples de entender e explicar o passo a passo.

## O problema

A instituição de microcrédito que apoia pequenos empreendedores da
periferia (costureiras, feirantes, mecânicos...) tinha um sistema que
negava o crédito automaticamente se a pessoa não tivesse renda formal
comprovada (carteira assinada). O problema é que a maioria das mulheres
chefes de família da comunidade trabalha de forma informal, e mesmo
pagando as contas certinho no bairro elas eram reprovadas quase sempre
(95% de rejeição). Ou seja, o sistema tava excluindo gente que na
prática é boa pagadora, só porque não tem CLT.

O objetivo desse trabalho foi criar um novo jeito de decidir a
aprovação do crédito que não dependa só da renda formal, e sim de um
"Score Social" baseado no comportamento financeiro da pessoa.

## Como o programa decide (fluxo)

1. O programa pergunta o Score Social da pessoa (0 a 100). Esse valor
   representaria coisas como: histórico de pagamento no bairro, tempo
   que o negócio funciona, referências de vizinhos, pagamento de
   contas de água/luz etc. Isso é avaliado PRIMEIRO.
2. Depois pergunta a Renda Formal CLT (pode ser 0, se a pessoa for
   informal).
3. Se o Score Social for muito alto (>= 80), o crédito já é aprovado
   direto, não importa a renda.
4. Se não, o programa calcula uma nota final juntando 70% do Score
   Social + 30% da renda (transformada em pontos), e se essa nota
   passar de 60, aprova. Se não passar, reprova.

A ideia principal é que a renda formal NUNCA sozinha reprova alguém.
Ela só soma pontos extra se existir, mas quem não tem CLT não é
penalizado por isso - só não ganha o bônus.

## Por que esses pesos (70% / 30%)?

Coloquei 70% pro Score Social porque na prática, pra esse público, o
comportamento de pagamento no bairro/comunidade é um indicador mais
forte de quem vai pagar o empréstimo do que ter ou não carteira
assinada. Muita gente informal tem renda estável (mesmo sem CLT) e
paga tudo em dia, então faz mais sentido dar mais peso pro
comportamento real da pessoa do que pro tipo de vínculo empregatício.

Os outros 30% ficaram pra renda formal porque ela ainda é um dado
relevante (mostra estabilidade financeira), só que não pode ser
eliminatória como era antes. Por isso ela funciona só como um "bônus":
quem tem renda formal ganha pontos extra, mas quem não tem não perde
nada por causa disso.

### Sobre a regra do Score >= 80 aprovar direto

Enquanto eu tava testando o programa percebi um problema: como o peso
máximo do score social é 70%, uma pessoa informal com um score muito
bom (tipo 85) ficava com só 59,5 pontos no final - ou seja, reprovada
por meio ponto, só porque não tinha renda formal. Isso ia acontecer
bem no exemplo do enunciado (a costureira com ótimo histórico sendo
reprovada), então eu resolvi colocar uma regra extra: se o score social
for 80 ou mais, o crédito é aprovado de qualquer forma, sem precisar
da renda. Assim o sistema não repete o mesmo erro do sistema antigo.

## Sobre a nota de corte (60 pontos)

Escolhi 60/100 porque é um valor que exige um comportamento social
razoavelmente bom pra aprovar, mas ainda dá pra chegar nele tanto por
quem tem só o score social bom quanto por quem tem renda formal e um
score social mediano. Não achei certo deixar muito baixo (aprovaria
gente com histórico ruim) nem muito alto (voltaria a excluir demais).

## LGPD - proteção dos dados

Como o sistema mexe com dados financeiros de gente da periferia, que é
um público mais vulnerável, é importante pensar em como proteger esses
dados:

- O programa só usa dois números pra calcular o score (Score Social e
  Renda). Não usa nome, CPF, endereço nem nada que identifique a
  pessoa diretamente dentro da lógica de cálculo.
- O score não pode ser calculado usando coisas como raça, gênero,
  religião etc, porque isso seria discriminação disfarçada de
  "critério técnico".
- Pela LGPD (art. 20), a pessoa tem direito de pedir revisão de uma
  decisão tomada só por um sistema automático. Então o ideal é que a
  cooperativa sempre tenha um jeito da pessoa contestar uma reprovação
  e pedir pra um analista humano olhar o caso, não deixar 100% na mão
  do programa.
- Os dados (principalmente os de renda e histórico de pagamento)
  precisam ficar guardados de forma segura, com acesso restrito só pra
  quem realmente precisa mexer neles.
- A pessoa tem que saber, antes de passar os dados, pra que eles vão
  ser usados (calcular o score pra dar o crédito) - de um jeito
  simples de entender, já que nem todo mundo tem facilidade com termo
  técnico/jurídico.

## Impacto financeiro estimado

Pra ter uma ideia se vale a pena pra cooperativa, fiz uma estimativa
bem simples baseada nos números do enunciado:

- Se tiver uns 1000 possíveis clientes informais por ano, e antes só
  5% eram aprovados (uns 50 pessoas), com ticket médio de R$ 1.500 por
  crédito, isso dava só uns R$ 75.000 de crédito liberado por ano pra
  esse público.
- Se com o novo sistema a taxa de aprovação subir pra uma faixa mais
  realista, tipo 40% a 60% (não é aprovar todo mundo, só corrigir a
  exclusão indevida), isso já daria entre 400 e 600 aprovações por
  ano, ou seja, algo entre R$ 600.000 e R$ 900.000 de crédito liberado.
- Isso representa bem mais receita de juros pra cooperativa, além de
  ajudar mais gente da comunidade a sair do crédito informal (que
  costuma ter juros bem mais altos, tipo agiotagem).

Só que é importante lembrar que isso é uma estimativa. O ideal seria a
cooperativa testar esse modelo primeiro com um grupo pequeno (tipo uns
100 clientes aprovados só pelo novo critério) pra ver se a taxa de
inadimplência bate com o esperado antes de aplicar pra todo mundo. Se
o Score Social realmente for um bom indicador de quem paga em dia, os
números tendem a se confirmar, mas isso só dá pra saber testando na
prática.

## Como rodar

No terminal, dentro da pasta do projeto:

```
python3 src/triagem.py
```

O programa vai pedir o Score Social e a Renda Formal, e no final mostra
"Resultado: Aprovado" ou "Resultado: Reprovado".