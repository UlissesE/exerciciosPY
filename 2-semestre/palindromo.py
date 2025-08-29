def palindromo(string):
    inicio = 0
    final = len(string)-1
    while inicio < final:
        if string[inicio] != string[final]:
            return False
        if string[inicio] == string[final]:
            return True
        inicio += 1
        final -= 1

print(palindromo("abxa"))