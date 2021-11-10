alunos = []


def escola(opcao):
    if opcao == 1:
        print("===" * 15 + "INSERIR ALUNO" + "===" * 15)
        inserir(input("Insira o nome do aluno: ").title(), float(input("Insira a primeira nota: ")),
                float(input("Insira a segunda nota: ")))
        print("===" * 30)

    if opcao == 2:
        print("===" * 15 + "ALUNOS E MÉDIAS" + "===" * 15)
        for aluno in alunos:
            print(aluno)
        print("===" * 30)

    if opcao == 3:
        print("===" * 15 + "APROVADOS" + "===" * 15)
        aprovados()
        print("===" * 30)

    if opcao == 4:
        print("===" * 15 + "REPROVADOS" + "===" * 15)
        reprovados()
        print("===" * 30)

    if opcao == 5:
        print("===" * 15 + "SALVANDO EM DISCO" + "===" * 15)
        salvar()
        print("===" * 30)


def inserir(aluno, nota1, nota2):
    dicio = dict()
    media = (nota1 + nota2) / 2
    dicio.update({"Aluno": aluno,
                  "Nota 1": nota1,
                  "Nota 2": nota2,
                  "Média": media})
    return alunos.append(dicio)


def aprovados():
    num = 0
    for aluno in alunos:
        if aluno["Média"] >= 7:
            print(f"{aluno['Aluno']} está aprovado")
            num += 1
    if num == 0:
        print("Não há alunos aprovados")


def reprovados():
    num = 0
    for aluno in alunos:
        if aluno["Média"] < 7:
            print(f"{aluno['Aluno']} está reprovado")
            num += 1
    if num == 0:
        print(f"Não há alunos reprovados")


def salvar():
    with open("escola.txt", mode='w', encoding='UTF-8') as arq:
        for aluno in alunos:
            arq.write(str(aluno))
            arq.write("\n")


escolha = 0
while escolha != 6:
    print("===" * 15 + "ESCOLHA UMA OPÇÃO" + "===" * 15)
    print("1 - Inserir dados de alunos\n"
          "2 - Mostrar alunos cadastrados e suas médias\n"
          "3 - Mostrar alunos aprovados\n"
          "4 - Mostrar alunos reprovados\n"
          "5 - salvar em disco\n"
          "6 - Sair")
    print("===" * 30)
    escolha = int(input())
    escola(escolha)
    if escolha == 6:
        print("===" * 15 + "PROCESSO TERMINADO" + "===" * 15)
