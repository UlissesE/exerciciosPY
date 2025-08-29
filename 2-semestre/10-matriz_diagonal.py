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

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append('.')
        matriz.append(linha)
    return matriz

def diagonal(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    for i in range(tamanho):
        matriz[i][i] = "x"
    return matriz

def diagonal_inversa(tamanho):
    matriz = criar_matriz(tamanho, tamanho)
    for i in range(tamanho):
        i = tamanho - 1
        matriz[i][i] = "x"
    return matriz

print(diagonal_inversa(5))