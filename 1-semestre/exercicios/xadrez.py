def conta_rainhas_linha(linha):
    total = 0
    for letra in linha:
        if letra == 'q':
            total += 1
    return total

print(conta_rainhas_linha('..q.'))
print(conta_rainhas_linha('q.q.'))