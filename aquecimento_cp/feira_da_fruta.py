def preco_feira(frutas: list[str]) -> float:
    banana = 1.50
    tomate = 3.24
    abacate = 5.00

    subtotal = 0

    for fruta in frutas:
        if fruta == "banana":
            subtotal += 1.50
        if fruta == "tomate":
            subtotal += 3.24
        if fruta == "abacate":
            subtotal += 5.00

    return subtotal

    """
    Calcula o valor total de uma lista de frutas na feira.
    
    Args:
        frutas: Lista de strings com nomes de frutas ('banana', 'abacate' ou 'tomate')
        
    Returns:
        float: Valor total das frutas em reais
        
    Raises:
        ValueError: Se alguma fruta não for válida
    """
    

# Testes

assert preco_feira(['banana']) == 1.50, "Uma banana deve custar R$ 1.50"
assert preco_feira(['abacate', 'tomate']) == 8.24, "Abacate + tomate deve custar R$ 8.24"
assert preco_feira(['banana', 'banana']) == 3.00, "Duas bananas dá 3 reais"
assert preco_feira([]) == 0, "Lista vazia dá 0"

print("todos os testes passaram!")
print("E se fossem 50 tipos de frutas diferentes? No semestre que vem, vamos refazer essa funcao, usando dicionarios")