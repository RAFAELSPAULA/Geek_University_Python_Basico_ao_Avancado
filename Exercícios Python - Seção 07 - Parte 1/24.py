numero = []
altura = []

for i in range(10):
    numero.append(int(input(f"Digite o numero do {i + 1}º aluno:")))
    altura.append(float(input(f"Digite a altura do {i + 1}º aluno:")))

print(f"A altura do aluno mais alto é de: {max(altura)}m, esse aluno é o número {numero[altura.index(max(altura))]}"
      f"\nA altura do aluno mais baixo é de: {min(altura)}m, esse aluno é o número {numero[altura.index(min(altura))]}")
