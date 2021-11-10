# ex 26
from functools import wraps


def dec_trata_erros(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except(ValueError, TypeError, AttributeError, FileExistsError, FileNotFoundError) as err:
            print(f'Houve um erro: {err}')
            return True

    return wrapper


class CadastroAlunos:
    @dec_trata_erros
    def __init__(self, matricula, sobrenome, ano_nascimento):
        self.__matricula = matricula
        self.__sobrenome = sobrenome
        self.__ano_nascimento = int(ano_nascimento)

    @dec_trata_erros
    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    @dec_trata_erros
    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def get_sobrenome(self):
        return self.__sobrenome

    @dec_trata_erros
    def set_ano_nascimento(self, ano_nascimento):
        self.__ano_nascimento = ano_nascimento

    def get_ano_nascimento(self):
        return self.__ano_nascimento

    def get_aluno(self):
        return {i.replace('_CadastroAlunos__', ''): x for i, x in self.__dict__.items()}


@dec_trata_erros
def grava_arquivo(tot_aluno):
    tot_aluno = int(tot_aluno)
    lst = []
    for i in range(tot_aluno):
        print()
        aluno = CadastroAlunos(input('Digite a matrícula: '),
                               input('Digite o sobrenome: '),
                               input('Digite o ano de nascimento: '))

        lst.append(aluno.get_aluno())
        print()
        [print(i) for i in lst]
        print()

    lst = ['|'.join([f'{k}:{e}' for k, e in i.items()]) + '\n' for i in lst]

    with open('cadastro_alunos.txt', 'w', encoding='UTF-8') as arq:
        [arq.write(i) for i in lst]

    print('Cadastro salvo com sucesso no arquivo cadastro_alunos.txt')
    return ''


while grava_arquivo(input('Digite o total de alunas a ser gravado: ')):
    pass