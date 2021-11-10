try:
    with open('contatos.bin', 'rb') as f1:
        contatos = dict()
        a = f1.readlines()
        for i in a:
            items = i.strip().split(b';')
            items.pop()
            for k in items:
                chave_valores = k.split(b',')
                contatos[chave_valores[0].decode('utf8')] = \
                    [chave_valores[1].decode('utf8'), chave_valores[2].decode('utf8')]
    while True:
        a = input('Selecione a opção desejada:\n'
                  '1- Adicionar contato\n'
                  '2- Remover contato\n'
                  '3- Pesquisar contato pelo nome\n'
                  '4- Listar todos os contatos\n'
                  '5- Listar contatos que começam por uma letra específica\n'
                  '6- Imprimir aniversariantes do mês\n'
                  '7- Sair\n')
        if a == '1':
            while True:
                cod = input('Insira o nome do contato ou aperte "voltar" para voltar ao menu de opções: ')
                if cod == 'voltar':
                    break
                elif cod in [k[0] for k in contatos.items()]:
                    print('Este contato já existe')
                else:
                    tel = int(input(f'Insira o telefone a ser adicionado para {cod}: '))
                    dia = int(input(f'Insira o dia de aniversário de {cod}: '))
                    mes = int(input(f'Insira o mês de aniversário de {cod}: '))
                    contatos[cod] = [tel, f'{dia}/{mes}']
                    print('Contato adicionado')
        if a == '3':
            while True:
                cod = input('Insira o nome do contato ou aperte "voltar" para voltar ao menu de opções: ')
                if cod == 'voltar':
                    break
                elif cod in [k[0] for k in contatos.items()]:
                    print(f'Nome: {cod}; Tel: {contatos[cod][0]}; Aniversário: {contatos[cod][1]}')
                else:
                    print('contato não encontrado')
        if a == '4':
            while True:
                cod = input(
                    'Pressione "1" para mostrar todos os contatos ou digite "voltar para voltar ao menu anterior: ')
                if cod == '1':
                    for k in contatos.items():
                        print(f'Nome: {k[0]}  Telefone: {k[1][0]}  Aniversário: {k[1][1]}')
                if cod == 'voltar':
                    break
        if a == '5':
            while True:
                cod = input('Insira a letra que gostaria de pesquisar ou digite "voltar" para voltar ao'
                            ' menu anterior: ')
                if cod == 'voltar':
                    break
                else:
                    cod = cod.title()
                    if cod in [p[0][0] for p in contatos.items()]:
                        for i in contatos.items():
                            if cod == i[0][0]:
                                print(f'Nome: {i[0]}. Telefone: {i[1][0]}. Aniversário: {i[1][1]}')
                    else:
                        print('Nenhum contato encontrado')
        if a == '6':
            while True:
                mes = (input('Insira o mês do aniversário ou digite "voltar" para retornar ao menu anterior: '))
                if mes == 'voltar':
                    break
                else:
                    if int(mes) >= 10:
                        for k in contatos.items():
                            if int(k[1][1][-2::]) == int(mes):
                                print(f'{k[0]}, Aniversário: {k[1][1]}')
                            else:
                                print('Não há nenhum contato que faça aniversário nesse mês')
                    elif int(mes) < 10:
                        for k in contatos.items():
                            if int(k[1][1][-1::]) == int(mes):
                                print(f'{k[0]}, Aniversário: {k[1][1]}')
                            else:
                                print('Não há nenhum contato que faça aniversário nesse mês')

        if a == '2':
            cod = input(
                'Insira o nome do contato que deseja remover ou aperte "voltar" para voltar ao menu de opções: ')
            if cod not in [k[0] for k in contatos.items()]:
                print('Contato não encontrado')
            else:
                del (contatos[cod])
                print('Contato removido')

        if a == '7':
            with open('contatos.bin', 'wb') as f1:
                for i in contatos.items():
                    f1.write(f'{i[0]},{i[1][0]},{i[1][1]};'.encode('utf8'))
            break
except FileNotFoundError:
    contatos = dict()
    while True:
        a = input('Selecione a opção desejada:\n'
                  '1- Adicionar contato\n'
                  '2- Remover contato\n'
                  '3- Pesquisar contato pelo nome\n'
                  '4- Listar todos os contatos\n'
                  '5- Listar contatos que começam por uma letra específica\n'
                  '6- Imprimir aniversariantes do mês\n'
                  '7- Sair\n')
        if a == '1':
            while True:
                cod = input('Insira o nome do contato ou aperte "voltar" para voltar ao menu de opções: ')
                if cod == 'voltar':
                    break
                elif cod in [k[0] for k in contatos.items()]:
                    print('Este contato já existe')
                else:
                    tel = int(input(f'Insira o telefone a ser adicionado para {cod}: '))
                    dia = int(input(f'Insira o dia de aniversário de {cod}: '))
                    mes = int(input(f'Insira o mês de aniversário de {cod}: '))
                    contatos[cod] = [tel, f'{dia}/{mes}']
                    print('Contato adicionado')
        if a == '3':
            while True:
                cod = input('Insira o nome do contato ou aperte "voltar" para voltar ao menu de opções: ')
                if cod == 'voltar':
                    break
                elif cod in [k[0] for k in contatos.items()]:
                    print(f'Nome: {cod}; Tel: {contatos[cod][0]}; Aniversário: {contatos[cod][1]}')
                else:
                    print('contato não encontrado')
        if a == '4':
            while True:
                cod = input(
                    'Pressione "1" para mostrar todos os contatos ou digite "voltar para voltar ao menu anterior: ')
                if cod == '1':
                    for k in contatos.items():
                        print(f'Nome: {k[0]}  Telefone: {k[1][0]}  Aniversário: {k[1][1]}')
                if cod == 'voltar':
                    break
        if a == '5':
            while True:
                cod = input('Insira a letra que gostaria de pesquisar ou digite "voltar" para voltar ao'
                            ' menu anterior: ')
                if cod == 'voltar':
                    break
                else:
                    cod = cod.title()
                    if cod in [p[0][0] for p in contatos.items()]:
                        for i in contatos.items():
                            if cod == i[0][0]:
                                print(f'Nome: {i[0]}. Telefone: {i[1][0]}. Aniversário: {i[1][1]}')
                    else:
                        print('Nenhum contato encontrado')
        if a == '6':
            while True:
                mes = (input('Insira o mês do aniversário ou digite "voltar" para retornar ao menu anterior: '))
                if mes == 'voltar':
                    break
                else:
                    if int(mes) >= 10:
                        for k in contatos.items():
                            if int(k[1][1][-2::]) == int(mes):
                                print(f'{k[0]}, Aniversário: {k[1][1]}')
                            else:
                                print('Não há nenhum contato que faça aniversário nesse mês')
                    elif int(mes) < 10:
                        for k in contatos.items():
                            if int(k[1][1][-1::]) == int(mes):
                                print(f'{k[0]}, Aniversário: {k[1][1]}')
                            else:
                                print('Não há nenhum contato que faça aniversário nesse mês')

        if a == '2':
            cod = input(
                'Insira o nome do contato que deseja remover ou aperte "voltar" para voltar ao menu de opções: ')
            if cod not in [k[0] for k in contatos.items()]:
                print('Contato não encontrado')
            else:
                del (contatos[cod])
                print('Contato removido')

        if a == '7':
            with open('contatos.bin', 'wb') as f1:
                for i in contatos.items():
                    f1.write(f'{i[0]},{i[1][0]},{i[1][1]};'.encode('utf8'))
            break
