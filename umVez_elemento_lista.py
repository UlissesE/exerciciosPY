def umaVez(lista, elemento):
    contador = quantidade(lista,elemento)

    if contador == 1:
        return True
    return False

def quantidade(lista, elemento):
    contador = 0

    for v_lista in lista:
        if elemento == v_lista:
            contador += 1
    return contador

print(umaVez([11,22,33,44,55], 44))
print(umaVez([11,22,33,44,55,44], 44))
print(umaVez([11,22,33,44,55,55], 55))
print(umaVez([11,22,33,44,55], 55))
print(umaVez([11,22,33,44], 50))
print(umaVez([], 40))


    