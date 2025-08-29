toad = '''
.....xxxxxx.....
...xx..xxxxxx...
..x....xxxx..x..
.x....xxxxxx..x.
xxxxxxx....xxxxx
xx..xx......xxxx
x....x......xx.x
x....xx....xx..x
xx..xxxxxxxxx..x
xxxxxxxxxxxxxx.x
.xxx..x..x..xxx.
..x...x..x...x..
..x..........x..
...x........x...
....xxxxxxxx....
'''

toad2 = [['.', '.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.', '.', '.'],
['.', '.', '.', 'x', 'x', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.'],
['.', '.', 'x', '.', '.', '.', '.', 'x', 'x', 'x', 'x', '.', '.', 'x', '.', '.'],
['.', 'x', '.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', 'x', '.'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x'],
['x', 'x', '.', '.', 'x', 'x', '.', '.', '.', '.', '.', '.', 'x', 'x', 'x', 'x'],
['x', '.', '.', '.', '.', 'x', '.', '.', '.', '.', '.', '.', 'x', 'x', '.', 'x'],
['x', '.', '.', '.', '.', 'x', 'x', '.', '.', '.', '.', 'x', 'x', '.', '.', 'x'],
['x', 'x', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', 'x'],
['.', 'x', 'x', 'x', '.', '.', 'x', '.', '.', 'x', '.', '.', 'x', 'x', 'x', '.'],
['.', '.', 'x', '.', '.', '.', 'x', '.', '.', 'x', '.', '.', '.', 'x', '.', '.'],
['.', '.', 'x', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.'],
['.', '.', '.', 'x', '.', '.', '.', '.', '.', '.', '.', '.', 'x', '.', '.', '.'],
['.', '.', '.', '.', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '.', '.', '.', '.']]



mostra_matplot = False
mostra_string  = False
mostra_lista_de_listas = False
roda_testes = True




'''
A idéia desse arquivo é representar um desenho simples em AsciiART

Por exemplo, poderiamos ter 
.....xxxxxx.....
...xx..xxxxxx...
..x....xxxx..x..
.x....xxxxxx..x.
xxxxxxx....xxxxx
xx..xx......xxxx
x....x......xx.x
x....xx....xx..x
xx..xxxxxxxxx..x
xxxxxxxxxxxxxx.x
.xxx..x..x..xxx.
..x...x..x...x..
..x..........x..
...x........x...
....xxxxxxxx....

Esse desenho tem duas dimensões, largura e altura

Nosso plano é criar uma representação de um desenho.

Queremos representar o desenho.
.xa
x.x
.x.

Para isso, usaremos uma lista de listas, como a que segue
'''
minha_matriz = [['.','x','a'], 
                ['x','.','x'], 
                ['.','x','.'] ] 
'''

Repare que a primeira linha do desenho (.xa) está representada por uma lista
['.','x','a'] dentro da minha lista de listas.
'''

'''
Considere o seguinte desenho

mapa = [ ['.','x','a'], 
         ['c','.','l'], 
         ['.','k','.'] ] 
'''


#qual o valor presente na posicao 0,1? (ou seja, linha 0, coluna 1)?
valor1 = 'x'
# ao preencher esse valor, voce passa o teste 01a

#qual o valor presente na posicao 1,1? (ou seja, linha 1, coluna 1)?
valor2 = '.'
# ao preencher esse valor, voce passa o teste 01b

#qual o valor presente na posicao 2,1? (ou seja, linha 2, coluna 1)?
valor3 = 'k'
# ao preencher esse valor, voce passa o teste 01c



'''
Agora queremos começar a desenhar. Ou seja, a
colocar caracteres diferentes de '.' no nosso mapa.

Mas primeiro, façamos algumas preliminares
'''

'''
Implemente uma função primeira_linha,
que devolve a primeira linha do mapa.

Ou seja, se o mapa é
'''
mapa = [['.','b','.'],
        ['a','.','.'],
        ['.','.','c'],
        ['.','.','.']]
'''

Então primeira_linha(mapa) devolve a lista ['.','b','.']
'''
# se voce fez essa funcao corretamente, 
# vai passar o teste 02
def primeira_linha(mapa):
    return mapa[0]

'''
Implemente uma função linha_n. Ao chamar linha_n(mapa,3), pegamos, no mapa, a linha de índice 3 (lembre-se que essa é a quarta linha! A primeira tem indice 0, a segunda indice 1, a terceira indice 2)
'''
# se voce fez essa funcao corretamente, 
# vai passar o teste 03
def linha_n(mapa,linha):
    return mapa[linha]

'''
Implemente um funcao posicao(mapa,x,y). Ao chamar posicao(mapa,x,y), pegamos, no mapa, a linha de índice x, e depois o elemento de indice y dessa linha

Por exemplo, considerando o mapa

[['.','.','a'],
 ['b','c','d']]

Ao chamarmos posicao(1,2), pegamos a linha de indice 1 (ou seja, ['b','c','d'])
e retornamos o elemento de indice 2 (ou seja, 'd')
'''
# se voce fez essa funcao corretamente, 
# vai passar o teste 04
def posicao(mapa,linha,coluna):
    return mapa[linha][coluna]

'''
Exercício 05: Faremos uma função "coloca" para alterar o desenho. Suponha que começamos com
o seguinte desenho:

....
....
....
....

Ao fazer coloca(desenho,1,3,'a'), queremos adicionar a letra 'a' na linha de indice 1,
coluna de indice três. Ou seja, em l1 c3

   c0 c1 c2 c3
l0  .  .  .  .
l1  .  .  .  a
l2  .  .  .  .
l3  .  .  .  .

'''

def coloca(mapa, n_linha, n_coluna, simbolo):
    mapa[n_linha][n_coluna] = simbolo
    
    


'''
Se voce quiser marcar uma linha inteira com o mesmo simbolo, poderá usar a função a seguir

marca_linha(mapa,linha, simbolo)

Por exemplo, se o mapa era

....
....
....

E eu fizer marca_linha(mapa,2,'x')

Terei


....
....
xxxx

'''
# se voce fez essa funcao corretamente, 
# vai passar o teste 06
def marca_linha(mapa, n_linha, simbolo):
    linha = mapa[n_linha]
    for n_coluna in range(len(linha)):
        mapa[n_linha][n_coluna] = simbolo

'''
Também podemos fazer uma função analoga chamada marca_coluna, e passar o teste 07

Por exemplo, se o mapa era

....
....
....

E eu fizer marca_coluna(mapa,2,'x')

Terei


..x.
..x.
..x.
'''

def marca_coluna(mapa, coluna, simbolo):
    for linha in range(len(mapa)):
        mapa[linha][coluna] = simbolo

'''
Façamos agora uma função que monta um tabuleiro de xadrez.
Ou seja tabuleiro_xadrez(4) produz:

x.x.
.x.x
x.x.
.x.x

repare, marcamos com um x a posicao 0,0, e seguimos construindo o
tabuleiro a partir dai
'''
# teste 08
# def tabuleiro_xadrez(tamanho):
#     tabuleiro = []
#     count = 2

#     for _ in range(tamanho):
#         coluna = []
       
#         for _ in range(tamanho):
#             peca = "x" if count % 2 == 0 else "." 
#             coluna.append(peca)
#             count = count + 1

#         count += 1
#         tabuleiro.append(coluna)

#     return tabuleiro

def tabuleiro_xadrez(tamanho):
    tabuleiro = []

    for i in range(tamanho):
        coluna = []
       
        for j in range(tamanho):
            peca = "x" if ((i + j) % 2 == 0) else "." 
            # if (i + j) % 2 == 0:
            #     peca = "x"
            # else:
            #     peca = "."
            coluna.append(peca)

        tabuleiro.append(coluna)

    return tabuleiro




import unittest
import hashlib

class TestStringMethods(unittest.TestCase):

    def test01a_valor1(self):
        self.verifica_codigo(valor1,'54a2f7f92a5f975d8096af77a126edda7da60c5aa872ef1b871701ae')
    
    def test01b_valor2(self):
        self.verifica_codigo(valor2,'2727e5a04d8acc225b3320799348e34eff9ac515e1130101baab751a')
    
    def test01c_valor3(self):
        self.verifica_codigo(valor3,'5006bab5782456808d60bddfa64db2d13d90b2c5550ba1ff2b2acad7')
    

    def test02_primeira_linha(self):
        mapa = varias_linhas(3,4)
        self.assertEqual(primeira_linha(mapa),['.','.','.'])
        mapa = [['.','b','.'],
                ['a','.','.'],
                ['.','.','c'],
                ['.','.','.']]
        self.assertEqual(primeira_linha(mapa),['.','b','.'])

    def test03_linha_n(self):
        mapa = varias_linhas(3,4)
        self.assertEqual(linha_n(mapa,0),['.','.','.'])
        self.assertEqual(linha_n(mapa,2),['.','.','.'])
        mapa = [['.','b','.'],
                ['a','.','.'],
                ['.','.','c'],
                ['.','.','.']]
        self.assertEqual(linha_n(mapa,0),['.','b','.'])
        self.assertEqual(linha_n(mapa,2),['.','.','c'])

    def test04_posicao(self):
        mapa = varias_linhas(3,4)
        self.assertEqual(posicao(mapa,0,0),'.')
        self.assertEqual(posicao(mapa,1,2),'.')
        mapa = [['.','b','.'],
                ['a','.','.'],
                ['.','.','c'],
                ['.','.','.']]
        self.assertEqual(posicao(mapa,0,0),'.')
        self.assertEqual(posicao(mapa,0,1),'b')
        self.assertEqual(posicao(mapa,0,0),'.')
        self.assertEqual(posicao(mapa,1,0),'a')
        

    def test05_coloca(self):
        mapa = varias_linhas(3,4)
        alvo40 = [['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo40)
        coloca(mapa,0,0,'a')
        alvo41 = [['a','.','.'],
                  ['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo41)
        coloca(mapa,0,2,'b')
        alvo42 = [['a','.','b'],
                  ['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo42)
        coloca(mapa,1,2,'c')
        alvo43 = [['a','.','b'],
                  ['.','.','c'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo43)

    def test06_marca_linha(self):
        mapa = varias_linhas(3,4)
        alvo40 = [['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo40)
        marca_linha(mapa,0,'a')
        alvo41 = [['a','a','a'],
                  ['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo41)
        marca_linha(mapa,2,'b')
        alvo42 = [['a','a','a'],
                  ['.','.','.'],
                  ['b','b','b'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo42)
        
    def test07_marca_coluna(self):
        mapa = varias_linhas(3,4)
        alvo40 = [['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.'],
                  ['.','.','.']]
        self.assertEqual(mapa,alvo40)
        marca_coluna(mapa,0,'a')
        alvo41 = [['a','.','.'],
                  ['a','.','.'],
                  ['a','.','.'],
                  ['a','.','.']]
        self.assertEqual(mapa,alvo41)
        marca_coluna(mapa,2,'b')
        alvo42 = [['a','.','b'],
                  ['a','.','b'],
                  ['a','.','b'],
                  ['a','.','b']]
        self.assertEqual(mapa,alvo42)

    def test08_tabuleiro_xadrez(self):
        resultado4 = tabuleiro_xadrez(4)
        alvo4 = [['x','.','x','.'],
                 ['.','x','.','x'],
                 ['x','.','x','.'],
                 ['.','x','.','x']]
        self.assertEqual(resultado4,alvo4)
        resultado8 = tabuleiro_xadrez(8)
        alvo8 = [['x','.','x','.','x','.','x','.'],
                 ['.','x','.','x','.','x','.','x'],
                 ['x','.','x','.','x','.','x','.'],
                 ['.','x','.','x','.','x','.','x'],
                 ['x','.','x','.','x','.','x','.'],
                 ['.','x','.','x','.','x','.','x'],
                 ['x','.','x','.','x','.','x','.'],
                 ['.','x','.','x','.','x','.','x']]
        self.assertEqual(resultado8,alvo8)

    
    def verifica_codigo(self,valor_fornecido_aluno,codigo_correto):
        codigo_resp_aluno = hashlib.sha224(str(valor_fornecido_aluno).encode('utf-8')).hexdigest()
        if codigo_resp_aluno != codigo_correto:
            #print(codigo_resp_aluno)
            self.fail("valor fornecido nao bate com o esperado")


    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

''' Pode deletar as linhas do 'try' até o 'pass'
    Elas só existem pro meu gabarito, que eu uso durante a elaboração dos exercicios
'''
try:
    from desenho_gabarito import *
except SyntaxError:
    raise SyntaxError("erro de syntax no gabarito")
except:
    pass
''' delete até aqui, e não delete as linha abaixo '''

# essa função serve para gerar as matrizes que utilizaremos em nossos testes
# nao mexa nela, isso quebraria muita coisa no código
def varias_linhas(largura, altura):
    matriz = []
    for _ in range(altura): # _ eh uma variavel. Utilizamos esse nome de variavel, 
                            # por convencao, quando temos o plano de salvar valores na variavel
                            # mas nunca mais ler esses valores.
                            # Isso pode soar meio estranho.
                            # No caso, estamos usando essa variavel pra poder escrever o for,
                            # mas o valor dela não serve pra nada
        l = []
        for _ in range(largura):
            l.append('.')
        matriz.append(l)
    return matriz

def mostrar_matplot(matriz):
    # vamos ler essa função depois. Não se preocupe com ela agora. Ela está aqui só
    # para eu mostrar um desenho, definido como uma matriz do python
    # essa primeira linha diz que queremos usar uma biblioteca extra 
    # chamada matplotlib

    # se ela não estiver instalada, 
    # temos que rodar pip install matplotlib para que ela funcionasse
    import matplotlib.pyplot as plt

    # na nossa matriz, toad2, os pontos 'escuros' estão marcados com um 'x', e os pontos claros,
    # com um '.'. A biblioteca matplotlib prefere que os pontos escuros sejam marcados com um número
    # grande (no nosso caso, o número 10) e os pontos claros com um número pequeno (no nosso caso, 
    # o número 0)  
    # Vamos, então converter a matriz, linha a linha,
    # trocando sempre os caracteres 'x' e '.' pelos números 10 e 0.
    matriz_numerica = []
    for linha_x in matriz:
        linha_numeros = []
        for letra in linha_x:
            if letra == 'x' : linha_numeros.append(10)
            else: linha_numeros.append(0)
        matriz_numerica.append(linha_numeros)

    # essas funções sao da biblioteca matplotlib, não são interessantes de explicar hoje
    plt.imshow(matriz_numerica, cmap=plt.cm.Blues)
    plt.show()

def mostra_lista(lista):
    string = ""
    for elemento in lista:
        string += elemento
    return string

def mostra_listas(lista_de_listas):
    string = ""
    for lista in lista_de_listas:
        string_temp = ""
        for elemento in lista:
            string_temp += elemento
        string += string_temp
        string += '\n'
    return string

from pprint import pprint

def mostra_desenhos(desenho):
    if mostra_matplot:
        mostrar_matplot(desenho)
    if mostra_string:
        string = mostra_listas(desenho)
        print(string)
    if mostra_lista_de_listas:
        pprint(desenho, width=100)

mostra_desenhos(toad2)

if roda_testes:
    runTests()