def media(pessoas):
    soma = 0
    qtd = 0

    for pessoa in pessoas:
        if pessoa > 0.5 and pessoa < 3:
            soma += pessoa
            qtd += 1
    
    resultado = soma / qtd
    return resultado

def maiores(pessoas):
    mediana = media(pessoas)
    grandes = []

    for pessoa in pessoas:
        if pessoa > mediana:
            grandes.append(pessoa)

    if grandes == []:
        grandes = "Nenhum é maior"
    
    return grandes


print(media([1,1,1]))
print(media([2,2,3]))
print(media([1,1,0.4]))

print(maiores([1,1,1]))
print(maiores([2,2,3]))
print(maiores([1,1,0.4]))