# Para todos os exercicios desse arquivo, vamos trabalhar com listas de cartas
# como ['Ao','2o'], ['Ac','2p','3o','Ko']
# Ou seja, listas de strings, e cada string tem 2 caracteres, sendo o primeiro
# o tipo da carta, o segundo, o naipe da carta

# função busca_as_ouros:
# deve buscar a carta as de ouros numa lista de cartas
# retorna True se encontrou, False caso contrário
# lembrando: o as de ouros é a string 'Ao'
def busca_as_ouros(lista):
    return 'Ao' in lista

# Funçao carta repetida:
# Recebe duas listas, e verifica se existe uma mesma carta que aparece nas duas
# Retorna True se sim, False se não
# Por exemplo, se a lista 1 for ['Ao','2o'] e a lista 2 for ['Ac','2p','3o','Ko'] retorna False
# Por exemplo, se a lista 1 for ['Ao','2o'] e a lista 2 for ['Ac','2p','3o','Ao'] retorna True
def carta_repetida(lista1, lista2):
    for carta in lista1:
         if carta in lista2:
              return True
    return False

# funcao fala_naipe
# dada uma carta (lembrando: uma string de dois caracteres) retorna o naipe
# Por exemplo, fala_naipe('Ao') retorna 'o'
# Por exemplo, fala_naipe('Kc') retorna 'c'
# Ou seja: recebe uma string de dois caracteres, devolve o segundo
# Lembre-se, as strings, assim como as listas, começam com o indice 0
# s = "bacana"
# s[0] # é o valor 'b'
def fala_naipe(carta):
     return carta[1]
    

# Função naipe_repetido
# Verifica se as duas listas tem alguma carta do mesmo naipe
# Ou seja:
# * Se as duas tem uma carta de ouros, retorna True
# * Se as duas tem uma carta de copas, retorna True
# * a mesma coisa pra espadas e paus
# * Se não existir nenhum naipe em comum, retorna False
# Por exemplo, se a lista 1 for ['Ao','2o'] e a lista 2 for ['Ac','2p','3o','Ko'] retorna True
# Por exemplo, se a lista 1 for ['Ao','2o'] e a lista 2 for ['Ac','2p','3o','Ae'] retorna True
# Por exemplo, se a lista 1 for ['Ao','2o'] e a lista 2 for ['Ac','2p','3c','Ae'] retorna False
def naipe_repetido(lista1,lista2):
    for carta in lista1:
         for carta2 in lista2:
             if carta[1] == carta2[1]:
              return True
    return False

try: 
    from gabarito_cp4 import naipe_repetido, fala_naipe, busca_as_ouros, carta_repetida
except:
    pass

import unittest

class TestStringMethods(unittest.TestCase):
    def test01_busca_as_ouros(self):
         self.assertEqual(busca_as_ouros(["Ao"]),True)
         self.assertEqual(busca_as_ouros(["Ac"]),False)
         self.assertEqual(busca_as_ouros(["Ao","Ac","Ko"]),True)
         self.assertEqual(busca_as_ouros(["Ap","Ac","Ko"]),False)

    def test02_carta_repetida(self):
         self.assertEqual(carta_repetida(["Ao"],["Kc"]),False)
         self.assertEqual(carta_repetida(["Ao"],["Kc","Ao"]),True)
         self.assertEqual(carta_repetida(["Ao","2o","3o"],["Kc","Qc","2o","Jc"]),True)
         
    def test03_fala_naipe(self):
         self.assertEqual(fala_naipe("Ao"),"o")
         self.assertEqual(fala_naipe("Kc"),"c")
         self.assertEqual(fala_naipe("Kp"),"p")

    def test04_naipe_repetido(self):
        lista1=['Ao','2o']
        lista2a=['Ac','2p','3o','Ko']
        self.assertEqual(naipe_repetido(lista1,lista2a), True)
        lista2b=['Ac','2p','3o','Ae']
        self.assertEqual(naipe_repetido(lista1,lista2b), True)
        lista2c=['Ac','2p','3c','Ae']
        self.assertEqual(naipe_repetido(lista1,lista2c), False)


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()