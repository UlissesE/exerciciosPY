
# Faça uma função palindromo, que recebe uma string e responde True se ela é um palindromo, False caso contrário. Palindromo é uma string espelhada. palindromo(“aba”) deve retornar True, palindromo(“abacate”) deve retornar false

def palindromo(string):
    ultimo = len(string) - 1

    for letra in string:
        if letra != string[ultimo]:
             return False
        ultimo -= 1

    return True
    
    # return string == string[::-1] --> também funciona, reverte algo

import unittest

class TestesChiques(unittest.TestCase):
    
    def test01_pares(self):
        self.assertEqual(palindromo("abba"), True)
        self.assertEqual(palindromo("abbaabba"), True)
        self.assertEqual(palindromo("abca"), False)

    def test02_impares(self):
        self.assertEqual(palindromo("aba"), True)
        self.assertEqual(palindromo("abx"), False)

    def test03_pequenos(self):
        self.assertEqual(palindromo("a"), True)
        self.assertEqual(palindromo(""),  True)

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