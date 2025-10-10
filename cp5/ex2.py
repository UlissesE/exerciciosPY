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
Dada a id de um jogo, quantos gols ocorreram naquele jogo?
'''

def gols_do_jogo(dados,id_jogo):
    pass

'''
Dada uma data de jogo, no formato 2018-04-14, quantos gols ocorreram no total aquele dia?
'''

def gols_do_dia_por_data(dados,data):
    pass


'''
Dada id de um jogo, quantos gols ocorreram no total aquele dia?
Ou seja: descubra o dia do jogo, e some os gols de todos os jogos que ocorreram naquele dia,
inclusive o jogo que eu te passei
'''

def gols_do_dia_por_id(dados,id_jogo):
    pass


import unittest
#pode deletar as 4 linhas abaixo, até o pass dentro do except
try:
    from cp5_gabarito import *
except:
    pass

class TestStringMethods(unittest.TestCase):
    
    
    def test_001_gols_do_jogo(self):
        dados = pega_dados()
        self.assertEqual(gols_do_jogo(dados,'102095'),6)
        self.assertEqual(gols_do_jogo(dados,'102099'),2)
        self.assertEqual(gols_do_jogo(dados,'102128'),5)
        self.assertEqual(gols_do_jogo(dados,'102164'),1)
        
    def test_002_gols_do_dia_por_data(self):
        dados = pega_dados()
        self.assertEqual(gols_do_dia_por_data(dados,'2018-04-14'),7) # tres jogos, 1+4+2
        self.assertEqual(gols_do_dia_por_data(dados,'2018-04-21'),3) # dois jogos 1+2
        self.assertEqual(gols_do_dia_por_data(dados,'2018-04-28'),3) # um jogo com 3 gols
    
    def test_003_gols_do_dia_por_id(self):
        dados = pega_dados()
        self.assertEqual(gols_do_dia_por_id(dados,'102094'),7) # tres jogos, 1+4+2
        self.assertEqual(gols_do_dia_por_id(dados,'102107'),3) # dois jogos 1+2
        self.assertEqual(gols_do_dia_por_id(dados,'102119'),3) # um jogo com 3 gols
    

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
