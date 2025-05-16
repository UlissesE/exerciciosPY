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
