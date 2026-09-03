# Em vez de deixar esses numeros espalhados e escritos direto no meio
# do codigo (o que dificulta manutencao e auditoria), coloquei tudo
# organizado em um dicionario Python. Assim, se a empresa mudar algum
# limite (por exemplo, a meta de compliance ambiental), so precisa
# alterar aqui nesse arquivo, sem precisar mexer na logica do sistema
# em outros lugares.

REGRAS_NEGOCIO = {

    # regras de densidade da carga transportada
    "densidade_carga": {
        "minima_kg_por_m3": 300,     # abaixo disso, o caminhao ta rodando "vazio demais"
        "maxima_kg_por_m3": 800,     # acima disso, passa do limite seguro pro veiculo
        "unidade": "kg/m3",
    },

    # regras de compliance ambiental da frota (Green IT / sustentabilidade)
    "compliance_ambiental": {
        "limite_emissao_co2_kg_por_km": 2.5,     # limite maximo de emissao aceitavel
        "percentual_minimo_carga_retorno": 30,   # abaixo de 30% de carga no retorno = viagem ociosa
        "meta_reducao_emissao_percentual": 15,   # meta anual de reducao de emissao da frota
    },

    # custos usados pra calcular o prejuizo de rodar com pouca carga
    "custos_operacionais": {
        "custo_km_rodado_reais": 3.50,        # custo medio de rodar 1 km (manutencao, pedagio etc)
        "custo_combustivel_litro_reais": 6.20,
        "consumo_medio_km_por_litro": 3.0,    # quantos km o caminhao roda com 1 litro
    },
}


def calcular_custo_ociosidade(percentual_carga_retorno, distancia_km):
    """
    Calcula o custo de ociosidade quando o caminhao volta com menos de
    30% da carga (limite definido em compliance_ambiental).

    A ideia: se o caminhao voltou quase vazio, ele gastou combustivel e
    km rodado sem aproveitar a capacidade do veiculo. Isso gera custo
    financeiro extra pra empresa E impacto ambiental desnecessario
    (emissao de CO2 por um transporte pouco eficiente).
    """

    limite = REGRAS_NEGOCIO["compliance_ambiental"]["percentual_minimo_carga_retorno"]

    # se a carga de retorno ta dentro do limite, nao tem custo de ociosidade
    if percentual_carga_retorno >= limite:
        return 0

    custo_km = REGRAS_NEGOCIO["custos_operacionais"]["custo_km_rodado_reais"]
    custo_combustivel = REGRAS_NEGOCIO["custos_operacionais"]["custo_combustivel_litro_reais"]
    consumo_km_litro = REGRAS_NEGOCIO["custos_operacionais"]["consumo_medio_km_por_litro"]

    # custo total da viagem de volta (km rodado + combustivel gasto)
    custo_km_total = distancia_km * custo_km
    litros_gastos = distancia_km / consumo_km_litro
    custo_combustivel_total = litros_gastos * custo_combustivel

    custo_viagem = custo_km_total + custo_combustivel_total

    # a parte "ociosa" é proporcional ao espaco vazio que sobrou no caminhao
    # ex: se voltou com 10% de carga, 90% da viagem foi desperdicio
    percentual_ocioso = (100 - percentual_carga_retorno) / 100

    custo_ociosidade = round(custo_viagem * percentual_ocioso, 2)

    return custo_ociosidade


# teste rapido, só pra ver se ta calculando certo (rodar com: python3 src/config_negocio.py)
if __name__ == "__main__":
    print("Regras de negocio carregadas:")
    print(REGRAS_NEGOCIO)
    print()

    # exemplo: caminhao voltou com 10% de carga, numa viagem de 200 km
    exemplo_custo = calcular_custo_ociosidade(10, 200)
    print("Exemplo -> carga de retorno: 10%, distancia: 200km")
    print("Custo de ociosidade estimado: R$", exemplo_custo)