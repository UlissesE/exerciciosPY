def bobinha():
    lista = []
    i = 1
    while i < 8:
        lista.append(i)
        i += 1  
    return lista

a = bobinha()
assert(a == [1,2,3,4,5,6,7])