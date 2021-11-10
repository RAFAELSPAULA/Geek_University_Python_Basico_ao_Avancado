import pickle


class Despensa:
    __despensa: list = []
    __codigo: int = 0

    @classmethod
    def relatorio_geral(cls) -> list:
        for x in Despensa.__despensa:
            yield x

    @classmethod
    def entrada_produto(cls, codigo: int, quantidade: int):
        Despensa.__despensa[codigo][3] += quantidade

    @classmethod
    def retirada_produto(cls, codigo: int, quantidade: int):
        if Despensa.__despensa[codigo][3] >= quantidade:
            Despensa.__despensa[codigo][3] -= quantidade
        else:
            print(f'Não disponibilizamos dessa quantidade do produto {Despensa.__despensa[codigo][0]}')

    @classmethod
    def verificar_zerados(cls):
        contagem_zerados = 0
        for x in Despensa.__despensa:
            if x[3] == 0:
                contagem_zerados += 1
                return print(f'O produto {x[0]}, código {x[2]}, está com o estoque zerado')
        if contagem_zerados == 0:
            return print('Não produtos zerados no estoque')

    @classmethod
    def gravar_arquivo(cls):
        despensa = open('despensa.txt', 'wb')
        pickle.dump(Despensa.__despensa, despensa)

    def __init__(self, nome: str, descricao: str, quantidade: int):
        self.__nome = nome
        self.__descricao = descricao
        self.__codigo = Despensa.__codigo
        self.__quantidade = quantidade
        Despensa.__despensa.append([self.__nome, self.__descricao, self.__codigo, self.__quantidade])
        Despensa.__codigo += 1

    @property
    def nome_e_descricao(self):
        return f'{self.__nome} | {self.__descricao}'

    @property
    def quantidade(self):
        return f'{self.__nome} | Código: {self.__codigo} | Quantidade: {self.__quantidade}'