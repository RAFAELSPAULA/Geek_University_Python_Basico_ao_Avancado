def consumo(a, b, sinal):
    if sinal == '+':
        total = a + b
        if total < 8:
            print('Venda Carro')
        elif (total > 8) and (total < 14):
            print('Econômico')
        else:
            print('Super Econômico')
        return total
    elif sinal == '-':
        total = a - b
        if total < 8:
            print('Venda Carro')
        elif (total > 8) and (total < 14):
            print('Econômico')
        else:
            print('Super Econômico')
        return total
    elif sinal == '*':
        total = a * b
        if total < 8:
            print('Venda Carro')
        elif (total > 8) and (total < 14):
            print('Econômico')
        else:
            print('Super Econômico')
        return total
    elif sinal == '/':
        total = a / b
        if total < 8:
            print('Venda Carro')
        elif (total > 8) and (total < 14):
            print('Econômico')
        else:
            print('Super Econômico')
        return total


print(consumo(1, 15, '+'))

