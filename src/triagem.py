# LaunchLab UniFAP - Semana 1
# Desenvolva a logica corrigida abaixo para evitar a exclusao de trabalhadores informais

def calcular_triagem():
    print("--- SISTEMA DE MICROCRÉDITO INCLUSIVO UniFAP ---")
    
    # Entradas do sistema
    score_social = int(input("Digite o Score Social Alternativo (0-100): "))
    renda_formal = float(input("Digite a Renda Formal CLT (R$): "))
    
    # CODIGO COM ERRO (A ser corrigido pela celula):
    # O aninhamento abaixo rejeita quem tem renda zero, mesmo com score 100!
    if score_social >= 60:
        if renda_formal > 1500:
            print("Resultado: Aprovado")
        else:
            print("Resultado: Reprovado")
    else:
        print("Resultado: Reprovado")

if __name__ == "__main__":
    calcular_triagem()
