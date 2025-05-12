def nomes_muito_grandes(lista_nomes):
    nomes_grandes = []

    for nome in lista_nomes:
        if len(nome) > 10:
            nomes_grandes.append(nome)
    
    return nomes_grandes

    """
    Filtra uma lista de nomes e retorna apenas aqueles com mais de 10 letras.
    
    Args:
        lista_nomes (list): Lista contendo strings com nomes
        
    Returns:
        list: Nova lista contendo apenas os nomes com mais de 10 letras
    """
    pass

# Testes
assert nomes_muito_grandes(["Joao", "Constantinos"]) == ["Constantinos"], f"Erro no teste básico"
assert nomes_muito_grandes([]) == [], f"Erro no teste com lista vazia"
assert nomes_muito_grandes(["Ana", "Pedro", "Alexandrino"]) == ["Alexandrino"], f"Erro no teste com vários nomes"
assert nomes_muito_grandes(["Alexandrino", "Bernardinos", "Carlos"]) == ["Alexandrino", "Bernardinos"], f"Erro no teste com múltiplos nomes grandes"
assert nomes_muito_grandes(["Maria", "Jose", "Gabrielinos"]) == ["Gabrielinos"], f"Erro no teste com nome grande no final"

print("Todos os testes passam!")