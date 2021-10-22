carlos = float(input('Digite o salário do carlos: '))
joao = carlos / 3
print(f'Salário de joão {joao:.2f} reais')

meses = 0

while carlos > joao:
    carlos *= 1.02
    joao *= 1.05
    meses += 1


print(f'João levará {meses} meses para acumular/superar os rendimentos de Carlos ')
print(f'O rendimento de carlos é {carlos:.2f} reais e de João é {joao:.2f} reais')
