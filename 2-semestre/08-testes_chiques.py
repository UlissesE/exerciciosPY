def somar(a,b):
     return a+b

def multiplicar(lista):
     resposta = 1
     for elemento in lista:
          resposta = resposta*elemento
     return resposta

def soma_dois_primeiros(lista):
     if len(lista) < 2:
          return "Valores insuficientes"
     return lista[0]+lista[1]
     


import unittest

class TestesChiques(unittest.TestCase):
    def test01_somar(self):
        self.assertEqual(somar(1,2),3)
        self.assertEqual(somar(10,2),12)
    
    def test02a_multiplicar(self):
         self.assertEqual(multiplicar([1,2,3]),6)

    def test02b_multiplicar(self):
         self.assertEqual(multiplicar([9]),9)

    def test03a_soma_dois_primeiros(self):
         self.assertEqual(soma_dois_primeiros([9,10]),19)
         self.assertEqual(soma_dois_primeiros([1,2,3,4,5]),3)

    def test03b_soma_dois_primeiros(self):
         self.assertEqual(soma_dois_primeiros([9]),'valores insuficientes')
         self.assertEqual(soma_dois_primeiros([]) ,'valores insuficientes')




def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestesChiques)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

'''
Pode deletar o código abaixo, ele só serve
pra quando eu estou elaborando o exercicio
'''
try:
     from testes_chiques_gabarito import *
except:
     pass
'''Delete só até aqui'''

runTests()