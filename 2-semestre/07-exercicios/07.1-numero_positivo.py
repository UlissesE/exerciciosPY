numero_positivo = int(input("Insira um número. "))
print("Número positivo!") if numero_positivo > 0 else print("Número não positivo.")
print(f"\n")

numero_par = int(input("Insira outro número. "))
print("Número par!") if numero_par % 2 == 0 else print("Número ímpar.")
print(f"\n")

contem_letra_a = input("Escreva uma palavra. ").lower()
print("Contém letra 'a'") if "a" in contem_letra_a else print("Não contém letra 'a'")
print(f"\n")

temperatura = ''
while not temperatura.isdigit():
    temperatura = input("Insira uma temperatura (somente números): ")
    if not temperatura.isdigit():
        print("Apenas digitos :)")
temperatura = float(temperatura)

if temperatura >= 30:
    print("Temperatura alta!!!")
elif temperatura >= 15:
    print("Temperatura agradável")
else:
    print("Temperatura baixa")
print(f"\n")


numero_dez = int(input("Insira o número 10: "))
if numero_par == 10:
    print("Obrigado :D")
else: 
    print("Esse não é o número 10 :(")
print(f"\n")

impar_ou_par = int(input("Digite um número: "))
if impar_ou_par % 2 == 0:
    print("É par")
elif impar_ou_par % 2 == 1:
    print("É impar")
else:
    print("Número inválido")
print(f"\n")


senhas = ["senha123", "senha1234"]
senha = input("Insira sua senha: ")
if senha not in senhas:
    print("Acesso negado!")
else: 
    print("Acesso concedido!")

print(f"\n")

ano_de_nascimento = int(input("Em que ano você nasceu?"))
ano_atual = 2025
if ano_atual - ano_de_nascimento >= 18:
    print("Maior de idade")
else: 
    print("Menor de idade")
print(f"\n")

numero_negativo = int(input("Insira um número. "))
print("Número negativo!") if numero_positivo < 0 else print("Número não negativo.")
print(f"\n")


texto_usuario = ''
while not texto_usuario:
    texto_usuario = input("Digite um texto.")    
    if not texto_usuario:
        "Nenhum texto recebido"
print("Texto recebido!")

nota_do_aluno = ""
while not nota_do_aluno.isdigit():
    nota_do_aluno = int(input("Digite sua nota"))
    if not nota_do_aluno.isdigit():
        print("Digite dígitos.")
if nota_do_aluno >= 90:
    print("Conceito A")
elif nota_do_aluno >= 80:
    print("Conceito B")
elif nota_do_aluno >= 70:
    print("Conceito C")
else:
    print("Conceito D")


print(f"\n")


nota_do_aluno = ""
while not nota_do_aluno.isdigit():
    nota_do_aluno = int(input("Digite sua pontuação"))
    if not nota_do_aluno.isdigit():
        print("Digite dígitos.")
if nota_do_aluno >= 85:
    print("Excelente")
elif nota_do_aluno >= 80:
    print("Bom")
elif nota_do_aluno >= 70:
    print("Regular")
else:
    print("Insuficiente")

    