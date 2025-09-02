# def matriz_diagonal(tamanho):
#     matriz = []
#     for i in range(tamanho):
#         linha = []
#         for j in range(tamanho):
#             linha.append('.')
#         linha[i] = "x"
#         matriz.append(linha)
#     return matriz

# print(matriz_diagonal(5))

def criar_matriz_quadrada(tamanho):
    matriz = []
    
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append('.')
        matriz.append(linha)
    
    return matriz

# print(criar_matriz(5))

def diagonal(tamanho):
    matriz = criar_matriz_quadrada(tamanho)

    for i in range(tamanho):
        matriz[i][i] = "x"
    
    return matriz

# print(diagonal(5))

def diagonal_inversa(tamanho):
    matriz = criar_matriz_quadrada(tamanho)

    for i in range(tamanho):
        j = (tamanho - 1) - i
        matriz[i][j] = 'x'

    return matriz

# print(diagonal_inversa(5))

def duas_diagonais(tamanho):
    matriz = criar_matriz_quadrada(tamanho)

    for i in range(tamanho):
        j = (tamanho - 1) - i
        matriz[i][i] = 'x'
        matriz[i][j] = 'x'

    return matriz

# print(duas_diagonais(5))


def matriz_bordas(tamanho):
    matriz = criar_matriz_quadrada(tamanho)

    for coluna in range(tamanho):
        matriz[coluna][0] = 'x'
        matriz[coluna][tamanho - 1] = 'x'

        matriz[0][coluna] = 'x'
        matriz[tamanho-1][coluna] = 'x'
        
    return matriz

# print(matriz_bordas(5))

def coluna(matriz, n_coluna):
    elementos_coluna = []

    for linha in matriz:
        elementos_coluna.append(linha[n_coluna])

    return elementos_coluna

print(coluna(duas_diagonais(5),0))
print(coluna(duas_diagonais(5),1))
print(coluna(duas_diagonais(5),2))