# Sistema de Score de Microcredito Inclusivo
# Trabalho de Sistemas de Informacao - UniFAP
#
# O sistema antigo da cooperativa so aprovava credito pra quem tinha
# carteira assinada (CLT). Isso excluia quase todo mundo que trabalha
# informal (costureira, feirante, mecanico), mesmo pagando as contas
# certinho. Esse programa calcula um Score Social e usa ele como
# criterio principal, em vez de depender só da renda formal.

print(" SISTEMA DE TRIAGEM DE MICROCREDITO ")
print()

# pede o score social ate a pessoa digitar um numero valido entre 0 e 100
score_social = -1
while score_social < 0 or score_social > 100:
    entrada = input("Digite o Score Social (0 a 100): ")
    try:
        score_social = float(entrada)
    except:
        print("isso ai nao é um numero valido")
        score_social = -1
        continue

    if score_social < 0 or score_social > 100:
        print("o score tem que ser entre 0 e 100")

# pede a renda formal (pode ser 0 se a pessoa for informal)
renda = -1
while renda < 0:
    entrada = input("Digite a Renda Formal CLT (0 se nao tiver): ")
    try:
        renda = float(entrada)
    except:
        print("digita um numero, ex: 1200.50")
        renda = -1
        continue

    if renda < 0:
        print("a renda nao pode ser negativa")

# calcula o bonus da renda (de 0 a 100), com teto de 3000
if renda <= 0:
    bonus_renda = 0
elif renda >= 3000:
    bonus_renda = 100
else:
    bonus_renda = (renda / 3000) * 100

# calcula a nota final: 70% score social + 30% bonus da renda
score_final = (score_social * 0.7) + (bonus_renda * 0.3)
score_final = round(score_final, 2)

print()
print("Score social:", score_social)
print("Renda formal:", renda)
print("Score final (70% social + 30% renda):", score_final)
print()

# decide o resultado
# regra 1: se o score social for muito alto (>=80), aprova direto,
# nao importa a renda. Coloquei essa regra porque sem ela, uma pessoa
# informal com score 85 ficava com só 59,5 no final e era reprovada
# por pouco, o que repetiria o mesmo problema do sistema antigo.
if score_social >= 80:
    print("Resultado: Aprovado")
elif score_final >= 60:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")