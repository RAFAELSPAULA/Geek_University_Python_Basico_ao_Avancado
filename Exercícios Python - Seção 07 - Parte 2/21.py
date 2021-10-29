matriz = []
matrizA = []
matrizSoma = []
matrizSub = []
possiveis = 'abcdABCD'
for l in range(0, 2):
    matriz.append([])
    matrizA.append([])
    matrizSoma.append([])
    matrizSub.append([])
    for c in range(0, 2):
        print()
        matriz[l].append(float(input(f'Digite um número para linha {l} e coluna {c} da matriz A:')))
        matrizA[l].append(float(input(f'Digite um número para linha {l} e coluna {c} da matriz B:')))
        matrizSoma[l].append(matriz[l][c] + matrizA[l][c])
        matrizSub[l].append(matriz[l][c] - matrizA[l][c])
print()
print('MENU DE OPÇÕES:\n'
      'A - Somar as duas matrizes\n'
      'B - Subtrair a primeira matriz da segunda\n'
      'C - Adicionar uma consntante nas duas matrizes\n'
      'D - Imprimir as matrizes\n')
while True:
    op = input('Digite a opção desejada:')
    print()
    if op not in possiveis or len(op) == 0:
        print('Opção inválida!')
    else:
        if op == 'a':
            print(f'O resultado da soma entre a matriz A e a matriz B é:')
            for x in matrizSoma:
                print(x)
            break
        elif op == 'b':
            print(f'O resultado da soma entre a matriz A e a matriz B é:')
            for x in matrizSub:
                print(x)
            break
        elif op == 'c':
            constante = float(input('Digite um valor para a constante:\n'))
            matriz[0].append((constante,))
            matriz[1].append((constante,))
            matrizA[0].append((constante,))
            matrizA[1].append((constante,))
            print('MATRIZ MODIFICADA A')
            for c in matriz:
                print(c)
            print()
            print('MATRIZ MODIFICADA B')
            for d in matrizA:
                print(d)
            break
        else:
            print('MATRIZ A')
            for x in matriz:
                print(x)
            print()
            print('MATRIZ B')
            for x in matrizA:
                print(x)
        break
print('FIM DO PROGRAMA!')