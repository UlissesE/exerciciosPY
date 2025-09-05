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

# as duas funções abaixo também são dadas de graça, mas talvez você acabe usando 
# elas no seu código

def calculaLargura(matriz):
    return len(matriz[0]) #o tamanho da primeira linha

def calculaAltura(matriz):
    return len(matriz) #o numero de linhas da matriz

# crie a função ponto_dentro
# ela recebe uma matriz, um número de linha "l1" e um número de coluna "c1"
# e responde True se esse ponto (l1,c1) está dentro da matriz
# False se o ponto cai fora
#
def ponto_dentro(matriz, linha, coluna):
    if linha < len(matriz):
        if coluna < len(matriz[linha]):
            return True
    return False
            
    
# crie a função desenha_ponto_seguro
# ela recebe uma matriz, um número de linha "l1" e um número de coluna "c1"
# e desenha um 'x' na posição correspondente se esse ponto (l1,c1) está dentro da matriz
# Não faz nada se o ponto cai fora
 
def desenha_ponto_seguro(matriz, linha, coluna):
    
    if ponto_dentro(matriz, linha, coluna):
        matriz[linha][coluna] = 'x'

try:    
    from gabarito_cp4 import ponto_dentro, desenha_ponto_seguro
except:
    pass

import unittest

class TestStringMethods(unittest.TestCase):
    def test01a_dentro(self):
        m = cria_matriz(5,4)
        self.assertEqual(ponto_dentro(m,1,1),True)
        self.assertEqual(ponto_dentro(m,2,1),True)
        self.assertEqual(ponto_dentro(m,3,2),True)
        self.assertEqual(ponto_dentro(m,8,8),False)
        self.assertEqual(ponto_dentro(m,6,2),False)
        self.assertEqual(ponto_dentro(m,3,6),False)
        self.assertEqual(ponto_dentro(m,2,2),True)

    def test01b_dentro_limites(self):
        m = cria_matriz(5,4)
        self.assertEqual(ponto_dentro(m,0,0),True)
        self.assertEqual(ponto_dentro(m,4,3),True)
        self.assertEqual(ponto_dentro(m,5,3),False)
        self.assertEqual(ponto_dentro(m,4,4),False)
        self.assertEqual(ponto_dentro(m,2,4),False)

        m2 = cria_matriz(6,6)
        self.assertEqual(ponto_dentro(m2,0,0),True)
        self.assertEqual(ponto_dentro(m2,5,5),True)
        self.assertEqual(ponto_dentro(m2,5,6),False)
        self.assertEqual(ponto_dentro(m2,6,5),False)
        self.assertEqual(ponto_dentro(m2,6,2),False)



    def test02a_desenha_ponto(self):
        m = cria_matriz(5,5)
        desenha_ponto_seguro(m,0,0)
        resposta1 = 'x....\n.....\n.....\n.....\n.....\n'
        self.assertEqual(mostra_matriz(m), resposta1)

        desenha_ponto_seguro(m,3,3)
        resposta2 = 'x....\n.....\n.....\n...x.\n.....\n'
        self.assertEqual(mostra_matriz(m), resposta2)

        desenha_ponto_seguro(m,7,7)
        self.assertEqual(mostra_matriz(m), resposta2)

        desenha_ponto_seguro(m,5,5)
        self.assertEqual(mostra_matriz(m), resposta2)


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()

# m = cria_matriz(10,10)
# desenha_ponto_seguro(m,3,3)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,4,4)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,5,3)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,6,4)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,9,9)
# print(mostra_matriz(m))


# desenha_ponto_seguro(m,10,3)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,3,10)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,3,-1)
# print(mostra_matriz(m))

# desenha_ponto_seguro(m,7,9)
# print(mostra_matriz(m))
