class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def nome(self, nome2):
        self.__nome = nome2

    def idade(self, idade2):
        self.__idade = idade2

    def altura(self, altura2):
        self.__altura = altura2

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura


class Agenda:
    idade1 = altura1 = cad = ''
    lista_cadastro = []

    while cad != 'N' or len(lista_cadastro) <= 10:
        cad = str(input("Deseja cadastrar um indivíduo [S/N] ")).upper()
        if cad in 'Ss':
            nome1 = str(input("Digite o nome da pessoa "))
            try:
                idade1 = int(input("Digite a idade da pessoa "))
            except (TypeError, ValueError):
                print("Idade tem que ser número inteiro")
                break
            try:
                altura1 = float(input("Digite a altura da pessoa "))
            except (TypeError, ValueError):
                print("Altura tem que ser número")
                break
            else:
                lista_cadastro.append(Pessoa(nome1, idade1, altura1))
        else:
            print("Finalizando")
            break

    @staticmethod
    def remover_pessoa(nome1):
        for n in Agenda.lista_cadastro:
            a = n.__dict__
            for j in a.keys():
                if nome1 in a.values():
                    return Agenda.lista_cadastro.remove(n)
        print('Pessoa não encontrada')

    @staticmethod
    def buscar(nome2):
        for n in Agenda.lista_cadastro:
            a = n.__dict__
            for j in a.keys():
                if nome2 in a.values():
                    return print(f'{nome2} se encontra na posição {Agenda.lista_cadastro.index(n)}')
        print("Pessoa não encontrada no sistema!")

    @staticmethod
    def imprime_agenda():
        if len(Agenda.lista_cadastro) == 0:
            print("Agenda vazia!")
        else:
            for n in Agenda.lista_cadastro:
                print(n.__dict__)

    def imprimir_pessoa(self, index):
        if 0 <= index < len(self.lista_cadastro):
            print(f"Nome: {self.lista_cadastro[index].get_nome()}")
            print(f"Idade: {self.lista_cadastro[index].get_idade()}")
            print(f"Altura: {self.lista_cadastro[index].get_altura()}")
            return True
        else:
            print("Posição não existente")
            return False


Agenda.imprime_agenda()
print('=' * 100)
Agenda.remover_pessoa('ale')
print('=' * 100)
Agenda.imprime_agenda()
print('=' * 100)
Agenda.buscar('rafael')
print('=' * 100)
Agenda.imprimir_pessoa(Agenda, 0)
