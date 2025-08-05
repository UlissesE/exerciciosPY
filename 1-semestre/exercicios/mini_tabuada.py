def tabuada():
    for n in range(1,7):
        for i in range(1,7):
            print(f'{n}x{i}={n*i}', end='; ')
        print('') #um print normal de uma string vazia

 
tabuada()