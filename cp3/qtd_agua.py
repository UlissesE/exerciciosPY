def avaliar_consumo_agua(consumos_ml):
    agua_total = 0

    for qtd in consumos_ml:
        agua_total += qtd

    if agua_total < 2000:
        return 'insuficiente'
    elif agua_total < 3000:
        return 'suficiente'
    else:
        return 'excesso'

    """
    Avalia o consumo diário de água baseado em uma lista de quantidades em ml.
    
    Argumentoss:
        consumos_ml (list): Lista de quantidades de água em mililitros
        
    Retorna:
        str: 'insuficiente' (< 2000ml), 'suficiente' (>= 2000ml <= 3000ml), 'excesso' (> 3000ml)
    """
    

# Teste1
print(avaliar_consumo_agua([500, 500]))                       
assert avaliar_consumo_agua([500, 500]) == 'insuficiente'     # 1000ml < 2000ml


# Teste2
print(avaliar_consumo_agua([1000, 1000, 900]))              # suficiente
assert avaliar_consumo_agua([1000, 1000, 900]) == 'suficiente'  # 2900ml = 2,9L


# Teste3
print(avaliar_consumo_agua([1500, 1500, 1500]))              # excesso
assert avaliar_consumo_agua([1500, 1500, 1500]) == 'excesso'    # 4500ml > 3000ml

print('Todos os testes passaram!')