cont = 1
with open('arq_exe23_emp.txt', 'w') as arq:
    while cont <= 5:
        while True:
            fun_nome = input(f'Informe o nome do {cont}° funcionário                   : ')
            if fun_nome == '' or fun_nome == ' ' or len(fun_nome) > 20:
                print('Nome invalido, ou maior que 20 caracteres!')
            else:
                tam_1 = 20 - len(fun_nome)
                fun_nome += ' ' * tam_1
                break
        while True:
            profissao = input(f'Informe a profissão de {fun_nome}        : ')
            if profissao == '' or profissao == ' ' or len(profissao) > 20:
                print('Profissão invalida, ou maior que 20 caracteres!')
            else:
                tam_2 = 20 - len(profissao)
                profissao += ' ' * tam_2
                break
        while True:
            try:
                tempo_trab = int(input(f'Informe o tempo de trabalho de {fun_nome}: '))
            except ValueError:
                print('Valor invalido!')
            else:
                break
        print('-------------------------------------------------------------------------------------------------------')
        cont += 1
        arq.write(f'Funcionário: {fun_nome} | Profissão: {profissao} | Tempo de Trabalho: {tempo_trab} anos')
        arq.write('\n')