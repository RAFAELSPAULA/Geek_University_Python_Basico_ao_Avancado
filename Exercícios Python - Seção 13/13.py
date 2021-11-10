nome = []
fone = []
dig_fone = 1234567890

print('CADASTRO DE AGENDA TELEFONICA')

while dig_fone != 0:
    dig_nome = input(' > Digite o nome do contado: ')
    if dig_nome == '':
        print('   - Informação obrigatória!')
    elif dig_nome in nome:
        print('   - Contado já cadastrado!')
    else:
        try:
            dig_fone = int(input(f' > Informe o fone de {dig_nome}, ou "0" para finalizar: '))
        except ValueError:
            print(f'   - Valor inválido!')
        else:
            if dig_fone != 0:
                nome.append(dig_nome)
                fone.append(dig_fone)

with open('Agenda_Telefonica.txt', 'w') as arq:
    for i in range(len(nome)):
        arq.write(f'{nome[i]}: {fone[i]}\n')

