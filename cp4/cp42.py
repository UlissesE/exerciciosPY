
# Funções de graça
# Essas duas funções estão aqui só pra você conseguir gerar
# exemplos de matrizes e visualizar mais fácil
# Veja um exemplo de execução abaixo


def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        l = []
        for j in range(colunas):
            l.append('.')
        matriz.append(l)
    return matriz

def mostra_matriz(lista_de_listas):
    string = ""
    for lista in lista_de_listas:
        string_temp = ""
        for elemento in lista:
            string_temp += elemento
        string += string_temp
        string += '\n'
    return string

# exemplo de uso das duas funções fornecidas 'de graça'
# >>> matriz = cria_matriz(3,5)
# >>> mostra_matriz(matriz)
# '...\n...\n...\n...\n...\n'
# >>> print(mostra_matriz(matriz))
# ...
# ...
# ...
# ...
# ...


# exercicios

# crie uma função que troca um '.' da matriz por um 'x'
# ela recebe a matriz, o número da linha e o número da coluna,
# e altera essa posicao da matriz, colocando a letra 'x' nela
# Nao precisa se preocupar com pontos caindo fora! Os testes não fazem isso
def desenha_ponto(matriz, linha, coluna):
    matriz[linha][coluna] = 'x'

# crie uma função que, ao receber uma posicao da matriz, desenha
# um 'x' em 5 posicoes diferentes, formando um sinal de mais
# Exemplo
# >>> matriz2 = cria_matriz(5,5)
# >>> print(mostra_matriz(matriz2))
# .....
# .....
# .....
# .....
# .....
# 
# >>> desenha_sinal_de_mais(matriz2, 2,2)
# >>> print(mostra_matriz(matriz2))
# .....
# ..x..
# .xxx.
# ..x..
# .....
# Repare. ela recebeu a posição 2,2, que é o centro do mapa
# marcou um x em 2,2, um x acima, um x abaixo, um x a direita e um x a esquerda
# Nao precisa se preocupar com pontos caindo fora! Os testes não fazem isso

def desenha_sinal_de_mais(matriz, linha, coluna):
    matriz[linha][coluna] = 'x'

    matriz[linha][coluna+1] = 'x'
    matriz[linha][coluna-1] = 'x'

    matriz[linha-1][coluna] = 'x'
    matriz[linha+1][coluna] = 'x'
# daqui pra baixo só tem burocracia, não precisa olhar nada

try:
    from gabarito_cp4 import desenha_ponto, desenha_sinal_de_mais
except:
    pass

import unittest

class TestStringMethods(unittest.TestCase):
    def test01_desenha_ponto(self):
        m = cria_matriz(5,5)
        desenha_ponto(m,0,0)
        resposta1 = 'x....\n.....\n.....\n.....\n.....\n'
        self.assertEqual(mostra_matriz(m),resposta1)    
        desenha_ponto(m,2,2)
        resposta2 = 'x....\n.....\n..x..\n.....\n.....\n'
        self.assertEqual(mostra_matriz(m),resposta2)    

    def test02_desenha_sinal_de_mais(self):
        m = cria_matriz(5,5)
        desenha_sinal_de_mais(m,2,2)
        resposta3 = '.....\n..x..\n.xxx.\n..x..\n.....\n'
        self.assertEqual(mostra_matriz(m),resposta3)    

        m = cria_matriz(5,5)
        desenha_sinal_de_mais(m,1,1)
        resposta4 = '.x...\nxxx..\n.x...\n.....\n.....\n'
        self.assertEqual(mostra_matriz(m),resposta4)    
        
        


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()

# se quiser ver uns desenhos a mais, temos esse codigo abaixo

# m = cria_matriz(11,11)
# desenha_sinal_de_mais(m,3,3)
# print(mostra_matriz(m))

# desenha_sinal_de_mais(m,7,3)
# print(mostra_matriz(m))

# desenha_sinal_de_mais(m,7,7)
# print(mostra_matriz(m))

# desenha_sinal_de_mais(m,3,7)
# print(mostra_matriz(m))


