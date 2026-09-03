# src/config_negocio.py

REGRAS_NEGOCIO = {
    # Mapeamento de densidade para cálculo de volume real
    "materiais": {
        "PLASTICO": {"densidade_kg_por_m3": 200},
        "VIDRO": {"densidade_kg_por_m3": 800},
        "METAL": {"densidade_kg_por_m3": 400},
    },
    
    "frota": {
        "capacidade_maxima_m3": 20.0,
    },
    
    # Metas de sustentabilidade (Green IT)
    "compliance_ambiental": {
        "limite_emissao_co2_kg_por_km": 2.5,
        "percentual_minimo_carga_retorno": 30.0,
        "meta_reducao_emissao_percentual": 15.0,
    },
    
    # Custos para precificar o desperdício
    "custos_operacionais": {
        "custo_km_rodado_reais": 3.50,
        "custo_combustivel_litro_reais": 6.20,
        "consumo_medio_km_por_litro": 3.0,
    },
    
    # Regras de infraestrutura e processamento
    "governanca_ti": {
        "estrategia_processamento": "STREAMING_EVENTOS",
        "retencao_dados_hot_storage_dias": 90,
        "auditoria_log_ativa": True
    }
}


def calcular_custo_ociosidade(peso_kg: float, tipo_material: str, distancia_km: float) -> float:
    tipo_material = tipo_material.upper()
    if tipo_material not in REGRAS_NEGOCIO["materiais"]:
        raise ValueError("Material não cadastrado.")

    # 1. Converte o peso em volume real ocupado na caçamba
    densidade = REGRAS_NEGOCIO["materiais"][tipo_material]["densidade_kg_por_m3"]
    volume_m3 = peso_kg / densidade
    
    capacidade_max = REGRAS_NEGOCIO["frota"]["capacidade_maxima_m3"]
    percentual_carga = (volume_m3 / capacidade_max) * 100

    limite = REGRAS_NEGOCIO["compliance_ambiental"]["percentual_minimo_carga_retorno"]

    if percentual_carga >= limite:
        return 0.0

    # 2. Calcula o custo operacional total da viagem
    custo_km = REGRAS_NEGOCIO["custos_operacionais"]["custo_km_rodado_reais"]
    custo_comb = REGRAS_NEGOCIO["custos_operacionais"]["custo_combustivel_litro_reais"]
    consumo = REGRAS_NEGOCIO["custos_operacionais"]["consumo_medio_km_por_litro"]

    custo_viagem = (distancia_km * custo_km) + ((distancia_km / consumo) * custo_comb)

    # 3. Penaliza financeiramente apenas a porcentagem que faltou para atingir a meta
    fator_desperdicio = (limite - percentual_carga) / limite
    
    return round(custo_viagem * fator_desperdicio, 2)


if __name__ == "__main__":
    # Exemplo: 600kg de plástico em 200km. 
    # Volume será de 3m³ (15% da frota), ficando 15% abaixo da meta de 30%.
    custo = calcular_custo_ociosidade(peso_kg=600, tipo_material="PLASTICO", distancia_km=200)
    
    print(f"Custo de ociosidade estimado: R$ {custo}")