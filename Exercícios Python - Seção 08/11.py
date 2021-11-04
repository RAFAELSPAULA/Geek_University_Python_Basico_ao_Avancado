def aluno(letra, nota1, nota2, nota3):
    if letra == 'a':
        return (nota1 + nota2 + nota3) / 3
    elif letra == 'p':
        return ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5 + 3 + 2)
    else:
        return 'Somente letra a ou p'


print(aluno('c', 1, 1, 1))


