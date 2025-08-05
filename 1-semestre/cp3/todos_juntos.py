def calcular_conta(kwh, bandeira):
    verde = 0.622
    amarela = 0.666
    vermelha_1 = 0.685
    vermelha_2 = 0.764

    if bandeira == "verde":
        valor = kwh * verde
    elif bandeira == "amarela":
        valor = kwh * amarela
    elif bandeira == "vermelha1":
        valor = kwh * vermelha_1
    elif bandeira == "vermelha2":
        valor = kwh * vermelha_2
    else:
        mensagemErro = "ParâmetroBandeira errado"
        return mensagemErro
    
    return valor
    

# Testes
assert calcular_conta(100, 'verde') == 62.2
assert calcular_conta(150, 'amarela') == 99.9
assert calcular_conta(200, 'vermelha1') == 137.0
assert calcular_conta(250, 'vermelha2') == 191


print("Todos os testes passaram!")






def verificar_divisores(lista_numeros, numero_x):
    qtd_numeros_lista = len(lista_numeros)
    qtd_numeros_divisores = []

    for numero in lista_numeros:
        if (numero_x % numero) == 0:
            qtd_numeros_divisores.append(numero)
        else:
            pass
    
    if len(qtd_numeros_divisores) == len(lista_numeros):
        return True
    else:
        return False
    
    """
    Verifica se todos os números na lista são divisores do número dado.
    
    Argumentos:
        lista_numeros: Lista de números inteiros
        numero: Número inteiro a ser verificado
        
    Retorna:
        bool: True se todos os números são divisores, False caso contrário
    """


# Testes usando assert
assert verificar_divisores([1, 2], 4) == True, "Teste 1 falhou"
assert verificar_divisores([1, 3], 4) == False, "Teste 2 falhou"
assert verificar_divisores([2, 4], 12) == True, "Teste 3 falhou"
assert verificar_divisores([2, 3, 4], 12) == True, "Teste 4 falhou"
assert verificar_divisores([2, 5], 10) == True, "Teste 5 falhou"
assert verificar_divisores([1, 2, 5], 10) == True, "Teste 6 falhou"
assert verificar_divisores([1, 2, 5, 3], 10) == False, "Teste 7 falhou"

print("Todos os testes passaram!")






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







def eh_ano_bissexto(ano):
    if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
        return True
    else:
        return False

assert eh_ano_bissexto(2000) == True, f"Erro no teste do ano 2000"
assert eh_ano_bissexto(1900) == False, f"Erro no teste do ano 1900"
assert eh_ano_bissexto(2024) == True, f"Erro no teste do ano 2024"
assert eh_ano_bissexto(2023) == False, f"Erro no teste do ano 2023"
assert eh_ano_bissexto(2004) == True, f"Erro no teste do ano 2004"

print("Todos os testes passaram!")

def proximos_cinco_anos_bissextos(ano_atual):
    proximos_anos = []
    ano = ano_atual + 1
    while len(proximos_anos) < 5:
        if eh_ano_bissexto(ano):
            proximos_anos.append(ano)
        ano += 1
    return proximos_anos


    """
    Retorna uma lista com os próximos 5 anos bissextos após o ano atual.

    Args:
        ano_atual (int): O ano a partir do qual começar a busca

    Returns:
        list: Lista dos próximos 5 anos bissextos
    """

# Testes
assert proximos_cinco_anos_bissextos(2024) == [2028, 2032, 2036, 2040, 2044], "Teste falhou para ano 2024"
assert proximos_cinco_anos_bissextos(2023) == [2024, 2028, 2032, 2036, 2040], "Teste falhou para ano 2023"
assert proximos_cinco_anos_bissextos(2090) == [2092, 2096, 2104, 2108, 2112], "Teste falhou para ano 2090"
assert proximos_cinco_anos_bissextos(1590) == [1592, 1596, 1600, 1604, 1608], "Teste falhou para ano 1590"

print("Todos os testes passaram!")
