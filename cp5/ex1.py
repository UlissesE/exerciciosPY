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
Abaixo, a a funcao data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu. 

Se essa nao é uma id valida, ela devolve a string 'nao encontrado'.

Essa função já está pronta, e não deve ser alterada
'''
def data_de_um_jogo(dados,id_jogo):
    dic_jogos = (dados['fases']['2700']['jogos']['id'])
    if id_jogo not in dic_jogos: #nao eh valida
        return "nao encontrado"
    return dic_jogos[id_jogo]['data']

'''
Construa uma função no_mesmo_dia. Dada uma id de um jogo, ela retorna
uma lista de todos os jogos que ocorreram no mesmo dia (inclusive a id que você forneceu)

dica: existe a possibilidade de achar os jogos de uma data direto no dicionário, sem
precisar fazer um for

dica: para fazer esse exercicio e os seguintes, se familiarize com
dados['fases']['2700']['jogos']['id']
dados['fases']['2700']['jogos']['data']
no firefox -- se você não lembrar como abrir o arquivo ano2018.json no firefox, essa
informação está na apostila
'''

def no_mesmo_dia(dados,id_jogo):

    data_id_jogo = dados['fases']['2700']['jogos']['id'][id_jogo]['data']
    lista_de_datas = dados['fases']['2700']['jogos']['data']

    if data_id_jogo in lista_de_datas:
        
        return lista_de_datas[data_id_jogo] # Vai retornar a lista completa de jogos que aconteceram nesse dia :)
    


import unittest
#pode deletar as 4 linhas abaixo, até o pass dentro do except
try:
    from cp5_gabarito import *
except:
    pass

class TestStringMethods(unittest.TestCase):
    
    def test_000_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(data_de_um_jogo(dados,'102132'),'2018-05-06')
        self.assertEqual(data_de_um_jogo(dados,'102187'),'2018-06-06')
        self.assertEqual(data_de_um_jogo(dados,'102540'),'nao encontrado')

    def test_001_no_mesmo_dia(self):
        dados = pega_dados()
        self.assertIn('102096',no_mesmo_dia(dados,'102096'))
        self.assertIn('102103',no_mesmo_dia(dados,'102096'))
        self.assertIn('102095',no_mesmo_dia(dados,'102096'))
        self.assertNotIn('102094',no_mesmo_dia(dados,'102096'))
        self.assertNotIn('102097',no_mesmo_dia(dados,'102096'))
        self.assertNotIn('102274',no_mesmo_dia(dados,'102096'))
        
        self.assertIn('102275',no_mesmo_dia(dados,'102275'))
        self.assertIn('102283',no_mesmo_dia(dados,'102275'))
        self.assertIn('102274',no_mesmo_dia(dados,'102275'))
        self.assertNotIn('102097',no_mesmo_dia(dados,'102275'))
        self.assertNotIn('102096',no_mesmo_dia(dados,'102275'))



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
