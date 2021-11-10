import os
registros = dict()
while True:
    a = input('Selecione a opção desejada:\n'
              '1- Criar arquivo de dados\n'
              '2- Adicionar registro ao arquivo\n'
              '3- Remover um registro do arquivo\n'
              '4- Alterar o valor de venda de um registro\n'
              '5- Mostrar todos os registros na tela principal\n'
              '6- Excluir o arquivo de dados criado\n'
              '7- Sair\n')
    if a == '1':
        while True:
            cod_arq = input('Entre com o nome do arquivo a ser criado ou digite voltar para retornar ao menu'
                            ' anterior: ')
            if cod_arq == 'voltar':
                break
            else:
                a = open(f'{cod_arq}' + '.txt', 'w')
                for i in sorted(registros.items(), key=lambda x: x[0]):
                    a.write(f'Código: {i[0]}  Nome: {i[1][0]}  Venda: {i[1][1]}  Mês: {i[1][2]}\n')
                a.flush()
                os.fsync(a.fileno())
                a.close()
                print(f'Arquivo {cod_arq}.txt criado com sucesso.')
                break
    if a == '2':
        while True:
            cod = input('Insira o código do vendedor ou aperte "voltar" para voltar ao menu de opções: ')
            if cod == 'voltar':
                break
            else:
                if cod in [k[0] for k in registros.items()]:
                    print('Esse código já está em uso')
                elif cod in [k[1][0] for k in registros.items()]:
                    print('Esse nome já está cadastrado')
                else:
                    name = input('Insira o nome do vendedor: ')
                    venda = float(input('Insira o valor da venda: '))
                    while True:
                        mes = int(input('Insira o mês da venda: '))
                        if mes in [k[1][2] for k in registros.items()]:
                            print('Já existe um registro com esse mês.')
                        else:
                            registros[cod] = [name, venda, mes]
                            break
                    print('Registro adicionado')
    if a == '3':
        while True:
            cod = input('Digite o código ou nome do vendedor ou digite "voltar para voltar ao menu anterior: ')
            if cod == 'voltar':
                break
            else:
                if cod in [k[0] for k in registros.items()]:
                    del registros[cod]
                    print('Registro deletado')
                elif cod in [k[1][0] for k in registros.items()]:
                    for i in registros.items():
                        if cod == i[1][0]:
                            del registros[i[0]]
                            print('Registro deletado')
                else:
                    print('Registro não encontrado')
    if a == '4':
        while True:
            cod = input('Insira o código ou o nome do vendedor que gostaria de alterar o valor da venda ou'
                        'digite "voltar" para retornar ao menu anterior: ')
            if cod == 'voltar':
                break
            else:
                if cod in [k[0] for k in registros.items()]:
                    a = float(input(f'Insira o novo valor de venda para {registros[cod][0]}: '))
                    registros[cod][1] = a
                    print('Operação realizada')
                elif cod in [p[1][0] for p in registros.items()]:
                    a = float(input(f'Insira o novo valor de venda para {cod}: '))
                    for i in registros.items():
                        if cod == i[1][0]:
                            registros[i[0]][1] = a
                            print('Operação realizada')
                else:
                    print('Nenhum contato encontrado')
    if a == '5':
        while True:
            cod = input('Aperte "1" para imprimir todos os contatos na tela '
                        'ou digite "voltar" para retornar ao menu anterior: ')
            if cod == 'voltar':
                break
            else:
                ordenado = sorted(registros.items(), key=lambda x: x[0])
                for i in ordenado:
                    print(f'Código: {i[0]}  Nome: {i[1][0]}  Venda: {i[1][1]}  Mês: {i[1][2]}')
    if a == '6':
        while True:
            cod = input('Insira o nome do arquivo que deseja deletar ou '
                        'aperte "voltar" para voltar ao menu de opções: ')
            if cod == 'voltar':
                break
            else:
                cod += '.txt'
                try:
                    os.remove(f'/home/rafael/PycharmProjects/pythonProject/{cod}')
                    print(f'{cod} foi deletado com sucesso.')
                except FileNotFoundError:
                    print('Arquivo não encontrado')
    if a == '7':
        break
