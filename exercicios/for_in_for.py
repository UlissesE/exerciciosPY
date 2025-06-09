# lista = [
#     [1,2,3],
#     ['a','b','c'],
#     ['@','#','$']
# ]

# for i in lista:
#     for item in i:
#         print(item,i)

# def divisores(n):
#     divisores = []
#     for numero in range(1,n+1):
#         if n % numero == 0:
#             divisores.append(numero)
#         else:
#             pass
    
#     return divisores

# while True:
#     numero = int(input('Digite um número '))
#     print(f" Os divisores de {numero} são: {divisores(numero)}")

def primos():
    resposta = []
    for num in range(1,100):
        divisores = []
        for i in range(1, num+1):
            if num % i == 0:
                divisores.append(i)
        if len(divisores) == 2:
            resposta.append(num)
            
    
    return resposta

print(primos())
    