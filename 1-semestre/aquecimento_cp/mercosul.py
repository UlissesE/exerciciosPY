def digito_ou_letra(caractere):
            if caractere.isalpha():
                return 'letra'
            elif caractere.isdigit():
                return 'digito'
            else:
                return 'nenhum'


assert digito_ou_letra('a') != None, "sua funcao retornou None. Isso significa que você esqueceu de dar return"
assert digito_ou_letra('a') == 'letra'
assert digito_ou_letra('z') == 'letra'
assert digito_ou_letra('3') == 'digito'
assert digito_ou_letra('@') == 'nenhum'




def placa_valida(placa: str) -> bool:
    letras = 0
    numeros = 0

    for i in range(len(placa)):
        print(placa[i])
        if i < 3:
            if placa[i].isalpha():
                letras += 1
            else:
                return False
        elif i == 3:
            if placa[i] == '-':
                pass
            else:
                return False
        elif i > 3:
            if placa[i].isdigit():
                numeros += 1
            elif placa[i].isalpha():
                letras += 1
            else:
                return False
        
    if letras == 4 and numeros == 3:
        return True
    else:
        return False
        
    """
    Verifica se uma string representa uma placa válida do Mercosul.
    
    Args:
        placa: String com a placa 
        
    Returns:
        bool: True se a placa é válida (no formato LLL-DLDD), 
              False caso contrário
    """

# Testes
assert placa_valida('a') != None, "sua funcao retornou None. Isso significa que você esqueceu de dar return"
assert placa_valida("ABC-1D23") == True, "Placa válida"
assert placa_valida("XYZ-9Z99") == True, "Outra placa válida"
assert placa_valida("ABCD1D23") == False, "Mais de 3 letras"
assert placa_valida("ABC-DD23") == False, "Quarta posição não é dígito"
assert placa_valida("ABC-1DD2") == False, "Menos de 2 dígitos no final"
assert placa_valida("AB-1D234") == False, "Mais de 2 dígitos no final"
assert placa_valida("ABC-1D234") == False, "Tamanho incorreto"

print("passou todos os testes!")