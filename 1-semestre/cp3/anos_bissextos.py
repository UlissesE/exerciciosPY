def eh_ano_bissexto(ano):
    if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
        return True
    else:
        return False

assert eh_ano_bissexto(2000) == True, f"Erro no teste do ano 2000"
assert eh_ano_bissexto(1900) == False, f"Erro no teste do ano 1900"
assert eh_ano_bissexto(2024) == True, f"Erro no teste do ano 2024"
assert eh_ano_bissexto(2023) == False, f"Erro no teste do ano 2023"
assert eh_ano_bissexto(2004) == True, f"Erro no teste do ano 2004"

print("Todos os testes passaram!")

def proximos_cinco_anos_bissextos(ano_atual):
    proximos_anos = []
    ano = ano_atual + 1
    while len(proximos_anos) < 5:
        if eh_ano_bissexto(ano):
            proximos_anos.append(ano)
        ano += 1
    return proximos_anos


    """
    Retorna uma lista com os próximos 5 anos bissextos após o ano atual.

    Args:
        ano_atual (int): O ano a partir do qual começar a busca

    Returns:
        list: Lista dos próximos 5 anos bissextos
    """

# Testes
assert proximos_cinco_anos_bissextos(2024) == [2028, 2032, 2036, 2040, 2044], "Teste falhou para ano 2024"
assert proximos_cinco_anos_bissextos(2023) == [2024, 2028, 2032, 2036, 2040], "Teste falhou para ano 2023"
assert proximos_cinco_anos_bissextos(2090) == [2092, 2096, 2104, 2108, 2112], "Teste falhou para ano 2090"
assert proximos_cinco_anos_bissextos(1590) == [1592, 1596, 1600, 1604, 1608], "Teste falhou para ano 1590"

print("Todos os testes passaram!")
