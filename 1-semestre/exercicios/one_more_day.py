def mais_um(dia, hora, minuto):
    minuto = minuto + 1


    if minuto >= 60:
        hora = hora + (minuto // 60)
        minuto = minuto % 60

    
    if hora >= 24:
        dia += (hora // 24)
        hora = hora % 24

    if dia < 10:
        dia = f"0{dia}"

    if minuto < 10:
        minuto = f"0{minuto}"

    return f"{dia} {hora}:{minuto}" 



print(mais_um(8, 48, 8))
assert(mais_um(1, 1, 10) == '01 1:11')
assert(mais_um(2, 3, 59) == '02 4:00')
assert(mais_um(3, 1,35) == '03 1:36')
assert(mais_um(4, 3,12) == '04 3:13')
assert(mais_um(5, 23, 59) == '06 0:00')
