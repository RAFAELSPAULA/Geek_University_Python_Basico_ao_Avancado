"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas
mencionadas anteriormente obedece aos pesos:

* Trabalho Laboratório: 2;
* Avaliação Semestral: 3;
* Exame Final : 5;

De acordo com o resultado, mostre na tela se o aluno está:
* reprovado (média entre 0 e 2.9);
* recuperação (entre 3 e 4,9);
* Demais aprovado;

Faça todas as verificações necessárias.
"""
nota1 = float(input('Digite a nota da primeira avaliação: '))

if (nota1 < 0) or (nota1 > 10):
    print('Nota invalida')
else:
    nota2 = float(input('Digite a nota da segunda avaliação: '))
    if (nota2 < 0) or (nota2 > 10):
        print('Nota invalida')
    else:
        nota3 = float(input('Digite a nota da terceira avaliação: '))
        if (nota3 < 0) or (nota3 > 10):
            print('Nota invalida')
        else:
            pass

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)
print(f'Media: {media}')

if media < 2.9:
    print('Reprovado')
elif media > 4.9:
    print('Aprovado')
else:
    print('Recuperação')
