# Um exemplo de recursão básico.
# Recursão é quando uma função chama a si mesma.
# Lembre-se sempre de colocar breaks nessas funções, senão irão entrar em loop infinito

def contagem_regressiva(n):
    if n >= 0:
        print(n)
        contagem_regressiva(n - 1)
    else:
        return

# Essa função irá chamar a si mesma até n ser menor que 0 (n < 0)

# contagem_regressiva(997)

# Máximo de recursão em Python 3: 997 linhas

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

# numero = fatorial(100)
# print('{0:,}'.format(numero).replace(',','.'))

def soma(arr):
    if arr == []:
        return 0
    return arr[0] + soma(arr[1:])

lista = [1,2,3,40,5,6,7]

lista = sorted(lista, reverse=True)

# print(soma(lista))

def soma_items(arr):
    if arr == []:
        return 0
    return 1 + soma_items(arr[1:])


# print(soma_items(lista))

def maior_n_da_lista(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maior_n_da_lista(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

# print(maior_n_da_lista(lista))

def pesquisa_binaria_recursiva(array, item_procurado, menor=0, maior=None): 
    if maior is None:
        maior = len(array) -1 

    if menor > maior:
        return -1
    
    meio = (menor + maior) // 2 
    if array[meio] == item_procurado: 
        return meio 
    elif array[meio] > item_procurado: 
        return pesquisa_binaria_recursiva(array, item_procurado, menor, meio - 1) 
    elif array[meio] < item_procurado: 
        return pesquisa_binaria_recursiva(array, item_procurado, meio + 1, maior)

# lista = [10,20,30,40,50,60]
# print(pesquisa_binaria_recursiva(lista, 40))

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i < pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
# print(quicksort(lista))