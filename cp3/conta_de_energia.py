def calcular_conta(kwh, bandeira):
    verde = 0.622
    amarela = 0.666
    vermelha_1 = 0.685
    vermelha_2 = 0.764

    if bandeira == "verde":
        valor = kwh * verde
    elif bandeira == "amarela":
        valor = kwh * amarela
    elif bandeira == "vermelha1":
        valor = kwh * vermelha_1
    elif bandeira == "vermelha2":
        valor = kwh * vermelha_2
    else:
        mensagemErro = "ParâmetroBandeira errado"
        return mensagemErro
    
    return valor
    

# Testes
assert calcular_conta(100, 'verde') == 62.2
assert calcular_conta(150, 'amarela') == 99.9
assert calcular_conta(200, 'vermelha1') == 137.0
assert calcular_conta(250, 'vermelha2') == 191


print("Todos os testes passaram!")
