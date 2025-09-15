def conta_letras(string):
    dicionario = {}
    
    for letra in string:
        if letra not in dicionario:
            dicionario[letra] = 1
        else:
            dicionario[letra] += 1
    
    return dicionario

    return dicionario
dici_vazio = {}        
#conta_letras('banana').keys() == ["a","b","n"]
assert conta_letras('banana') == {"a":3, "b":1, "n":2}