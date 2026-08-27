# logica corrigida abaixo para evitar a exclusao de trabalhadores informais,
# adicionei um sistema de pontos que pode influenciar posivitavamente ou negativamente no score.

LIMIAR_APROVACAO = 60   # nota minima para ter direito ao beneficio
BONUS_MAX = 15          # quanto a renda formal pode SOMAR, no maximo
RENDA_TETO = 3000       # renda a partir da qual o bonus para de crescer

def calcular_triagem():
    print("--- SISTEMA DE MICROCRÉDITO INCLUSIVO UniFAP ---")
    print()

# 1) ENTRADA: SCORE SOCIAL
    
    score_social = -1
    while score_social < 0 or score_social > 100:
        entrada = input("Digite o Score Social Alternativo (0 a 100): ")
        try:
            score_social = float(entrada.replace(",", "."))
        except ValueError:
            print("  [!] Isso nao e um numero valido. Ex: 78")
            score_social = -1
            continue
        if score_social < 0 or score_social > 100:
            print("  [!] O score tem que ser entre 0 e 100.")

# 2) ENTRADA: RENDA FORMAL CLT
   
    renda_formal = -1
    while renda_formal < 0:
        entrada = input("Digite a Renda Formal CLT (0 se nao tiver): ")
        try:
            renda_formal = float(entrada.replace(",", "."))
        except ValueError:
            print("  [!] Digite um numero. Ex: 1200.50")
            renda_formal = -1
            continue
        if renda_formal < 0:
            print("  [!] A renda nao pode ser negativa.")

# 3) BONUS DA RENDA
    
    if renda_formal <= 0:
        bonus_renda = 0
    elif renda_formal >= RENDA_TETO:
        bonus_renda = BONUS_MAX
    else:
        bonus_renda = (renda_formal / RENDA_TETO) * BONUS_MAX

    # Nota final = comportamento no bairro + reforco da renda (teto de 100)
    score_final = score_social + bonus_renda
    if score_final > 100:
        score_final = 100
    score_final = round(score_final, 2)

# 4) DECISAO
    # A analise comeca SEMPRE pelo score social, nunca pela renda.

    print()
    print("Score social informado : %.2f" % score_social)
    print("Renda formal (CLT)     : R$ %.2f" % renda_formal)
    print("Bonus da renda         : + %.2f ponto(s)" % bonus_renda)
    print("Score final            : %.2f" % score_final)
    print()

    if score_social >= LIMIAR_APROVACAO:
        print("Resultado: Aprovado")
        print("Motivo: historico social suficiente por si so.")
    elif score_final >= LIMIAR_APROVACAO:
        print("Resultado: Aprovado")
        print("Motivo: o bonus da renda formal completou a nota minima.")
    else:
        print("Resultado: Reprovado")
        print("Motivo: score abaixo do minimo de %d pontos." % LIMIAR_APROVACAO)


if __name__ == "__main__":
    calcular_triagem()