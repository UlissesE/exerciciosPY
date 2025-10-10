import json
from pprint import pprint


'''
DICA Pycharm:
Nunca abra o arquivo pelo "file explorer" do windows. Você deve
* Abrir o pycharm sem o arquivo
* NAO criar um projeto (esse ano a gente nunca quer criar um projeto via pycharm
ele faz várias coisas complicadas que a gente nao precisa)
* Clicar file > open e selecionar a pasta onde você baixou o brasileirao.py e
o ano2018.json
* Para rodar, clicar em qualquer lugar do texto do arquivo, 
com o botão direito, e selecionar "run file in python console"
'''

'''
DICA VSCODE: para poder executar o arquivo py a partir do VSCODE,
é importante ter aberto a pasta certa

Se voce tem a seguinte estrutura de diretorios
nossa_materia > brasileirao > brasileirao.py
                             ano2018.json

Deve selecionar no VSCODE File > Open folder
e escolher a pasta brasileirao.
Se escolher nossa_materia, o python nao vai achar o arquivo ano2018.json
'''


def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados
dados2018 = pega_dados()

'''
Dadas as ids de dois times, id1 e id2, quais foram os dias em que esses times
jogaram um contra o outro? Retorne uma lista com essas datas
'''

def confrontos(dados,id1,id2):
    pass

import unittest
#pode deletar as 4 linhas abaixo, até o pass dentro do except
try:
    from cp5_gabarito import *
except:
    pass

class TestStringMethods(unittest.TestCase):
    
    
    def test_001_confrontos(self):
        dados = pega_dados()
        self.assertIn('2018-06-13',confrontos(dados,'1','17'))
        self.assertIn('2018-10-27',confrontos(dados,'1','17'))
        self.assertNotIn('2018-10-26',confrontos(dados,'1','17'))
        self.assertIn('2018-08-12',confrontos(dados,'695','6'))
        self.assertIn('2018-11-25',confrontos(dados,'695','6'))
        self.assertNotIn('2018-10-26',confrontos(dados,'695','6'))
        self.assertNotIn('2018-10-27',confrontos(dados,'695','6'))
        
    # as proximas funcoes nao sao testes
    def setUp(self):
        global dados2018
        del dados2018
        return super().setUp()

    def tearDown(self):
        global dados2018
        dados2018 = pega_dados()
        return super().tearDown()

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados

dados2018 = pega_dados()

if __name__ == '__main__':
    runTests()
