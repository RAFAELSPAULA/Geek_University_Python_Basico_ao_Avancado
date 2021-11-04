def consumo(km, l):
    gasto = km / l
    if gasto < 8:
        print('Venda o Carro!')
        return gasto
    elif (gasto > 8) and (gasto < 14):
        print('Econômico!')
        return gasto
    elif gasto > 14:
        print('Super Econômico!')
        return gasto


print(consumo(240, 20))
