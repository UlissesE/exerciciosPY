lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [10,20,30,40,50,60,70,80.90,100]
lista3 = [100, 200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]

def pesquisa_binaria(lista, item_buscado):
    low = 0
    high = len(lista) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (high + low) // 2
        answer = lista[mid]

        if answer == item_buscado:
            return f"{steps} operações"
        if answer > item_buscado:
            high = mid - 1
        else:
            low = mid + 1
        
    
    return None

# print(pesquisa_binaria(lista1, 7))
# print(pesquisa_binaria(lista2, 20))
# print(pesquisa_binaria(lista3, 100))


def pesquisa_simples(lista, item_buscado):
    passos = 0
    for item in lista:
        passos += 1
        if item == item_buscado:
            return f"{passos} operações"
    
    return None

print(pesquisa_simples(lista1, 7))
print(pesquisa_simples(lista2, 20))
print(pesquisa_simples(lista3, 2000))