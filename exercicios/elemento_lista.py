def achei(lista, elemento):
    for v_lista in lista:
        if elemento == v_lista:
            return True
    return False

assert(achei([11,22,33,44], 33))
assert(achei([10,20,30,40], 10))
assert(achei([21,32,43,54], 43))
assert(achei([11,22,33,44], 33))

    