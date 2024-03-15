import json

def calcular_estatisticas_faturamento(faturamento_diario):
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

def main():
    # Carrega os dados do faturamento mensal 
    with open('faturamento_mensal.json', 'r') as arquivo:
        faturamento_mensal = json.load(arquivo)
    
    # Filtra os dias sem faturamento e calcula a estatística do faturamento
    faturamento_diario = [valor for valor in faturamento_mensal.values() if valor != 0]
    menor_valor, maior_valor, dias_acima_media = calcular_estatisticas_faturamento(faturamento_diario)
    
    # Exibe os resultados
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

if __name__ == "__main__":
    main()
