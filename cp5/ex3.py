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


Dado um número de gols, há vários jogos em que esse foi o número exato de gols
Retorne a lista de todos os ids desses jogos

Não considere gols feitos no desempate, nem gols de penalti
(pode ignorar totalmente as chaves 'penalti1', 'penalti2', 
'desempate_time1' e 'desempate time2')
'''

def jogos_com_x_gols(dados,nro_gols):
    pass


import unittest
#pode deletar as 4 linhas abaixo, até o pass dentro do except
try:
    from cp5_gabarito import *
except:
    pass

class TestStringMethods(unittest.TestCase):
    
    
    def test_001_jogos_com_x_gols(self):
        dados = pega_dados()
        self.assertIn('102119', jogos_com_x_gols(dados,nro_gols=3))
        self.assertIn('102117', jogos_com_x_gols(dados,nro_gols=0))
        self.assertIn('102471', jogos_com_x_gols(dados,nro_gols=0))
        self.assertIn('102167', jogos_com_x_gols(dados,nro_gols=5))
        self.assertNotIn('102167', jogos_com_x_gols(dados,nro_gols=0))
        self.assertNotIn('102471', jogos_com_x_gols(dados,nro_gols=1))
        self.assertNotIn('102471', jogos_com_x_gols(dados,nro_gols=2))
        

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
