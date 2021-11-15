class Elevador:

    def __init__(self, andar=5, capacidade=5):
        self.__capacidade = capacidade
        self.__andar = andar
        self.__quantidade = 0
        self.__andar_atual = 0

    def entra(self):
        if self.__quantidade < self.__capacidade:
            self.__quantidade += 1
            return 'Entrou 1 pessoa'
        return 'Elevador chegou no limite!'

    def sai(self):
        if self.__quantidade != 0:
            self.__quantidade += 1
            return 'Saiu 1 pessoa'
        return 'A quantidade de pessoa já está em zero'

    def sobe(self):
        if self.__andar_atual < self.__andar:
            self.__andar_atual += 1
            return 'O elevador subiu 1 andar!'
        return 'O elevador já esta no seu ultimo andar!'

    def desce(self):
        if self.__andar_atual != 0:
            self.__andar_atual -= 1
            return 'O elevador desceu 1 andar!'
        return 'O elevador já está no térreo!'

    # Getters
    def get_capacidade_maxima(self):
        return self.__capacidade

    def get_andar(self):
        return self.__andar

    def get_quantidade(self):
        return self.__quantidade

    def get_andar_atual(self):
        return self.__andar_atual

    # Setters
    def set_capacidade_maxima(self, qnt):
        self.__capacidade = qnt

    def set_total_andar(self, qnt):
        self.__andar = qnt


elevador_central = Elevador()

print(elevador_central.desce())
print(elevador_central.sobe())
print(elevador_central.sobe())
print(elevador_central.sobe())
print(elevador_central.sobe())
print(elevador_central.sobe())
print(elevador_central.sobe())
print(elevador_central.entra())
print(elevador_central.entra())
print(elevador_central.entra())
print(elevador_central.entra())
print(elevador_central.entra())
print(elevador_central.entra())
print(elevador_central.entra())
print(elevador_central.desce())
