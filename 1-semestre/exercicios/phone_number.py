def sp(lista):
    lista_fora = []

    for i in lista:
        if i[0] != '1' or i[1] != '1':
            lista_fora.append(i)
    
    return lista_fora

listaSP = ['11943433751', '11956278655', '12955444331', '13943412751', '1555443221']

assert(sp(listaSP) == ['12955444331', '13943412751', '1555443221'])