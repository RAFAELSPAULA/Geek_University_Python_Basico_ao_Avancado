class Televisao:
    ligada = False

    def __init__(self, volume, canais):
        self.__volume = volume
        self.__canais = canais

    @classmethod
    def ligar(cls):
        if not Televisao.ligada:
            Televisao.ligada = True

    @classmethod
    def desligar(cls):
        if Televisao.ligada:
            Televisao.ligada = False

    @classmethod
    def mostra_estado(cls):
        if Televisao.ligada:
            estado = 'ligada'
        else:
            estado = 'desligada'
        return estado

    def aumentar_volume(self):
        if self.__volume < 100:
            self.__volume += 1
            print(f'Volume: {self.__volume}')
        else:
            self.__volume = 100
            print(f'Volume: {self.__volume}')

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
            print(f'Volume: {self.__volume}')
        else:
            self.__volume = 0
            print(f'Volume: {self.__volume}')

    def avancar_canal(self):
        if self.__canais < 150:
            self.__canais += 1
            print(f'Canal: {self.__canais}')
        else:
            self.__canais = 1
            print(f'Canal: {self.__canais}')

    def recuar_canal(self):
        if self.__canais > 1:
            self.__canais -= 1
            print(f'Canal: {self.__canais}')
        else:
            self.__canais = 150
            print(f'Canal: {self.__canais}')

    def seleciona_canal(self):
        canal = int(input('selecione o canal: '))
        self.__canais = canal
        print(f'Canal: {self.__canais}')


class ControloRemoto:
    def __init__(self, tv):
        self.__tv = tv

    def high_sound(self):
        self.__tv.aumentar_volume()

    def loud_sound(self):
        self.__tv.diminuir_volume()

    def next_channel(self):
        self.__tv.avancar_canal()

    def previous_channel(self):
        self.__tv.recuar_canal()

    def select_channel(self):
        self.__tv.seleciona_canal()


def menu_tv():
    print('=' * 100)
    print(f'{"MENU - CONTROLO REMOTO":^100}')
    print(f'{"**Televisão com pacote de 150 canais**":^100}')
    print('=' * 100)
    tv = Televisao(25, 5)
    controlo_remoto = ControloRemoto(tv)
    opc = 0
    while opc != 7:
        print(f'{"OPÇÕES":^40}')
        print('1 - Para ligar a Televisão')
        print('2 - Para aumentar o volume em uma unidade')
        print('3 - Para dimunuir o volume em uma unidade')
        print('4 - Avançar para o próximo canal')
        print('5 - Recuar para o canal abaixo ')
        print('6 - Selecionar um canal')
        print('7 - Para desligar a Televisão')
        print('=' * 100)
        try:
            opc = int(input('Escolha uma das 8 opções acima: '))
            if opc <= 0 or opc > 7:
                print('Opção inválida')
                print('=' * 100)
        except ValueError:
            print('Opção inválida')
            print('=' * 100)
        if opc == 1:
            tv.ligar()
            print(f'Televisão {tv.mostra_estado()}')
            print('=' * 100)
        if opc == 2:
            estado = tv.mostra_estado()
            if estado == "desligada":
                print(f'Televisão {tv.mostra_estado()}')
                print('Deve ligar primeiro a Televisão')
                print('=' * 100)
            else:
                controlo_remoto.high_sound()
                print('=' * 100)
        if opc == 3:
            estado = tv.mostra_estado()
            if estado == "desligada":
                print(f'Televisão {tv.mostra_estado()}')
                print('Deve ligar primeiro a Televisão')
                print('=' * 100)
            else:
                controlo_remoto.loud_sound()
                print('=' * 100)
        if opc == 4:
            estado = tv.mostra_estado()
            if estado == "desligada":
                print(f'Televisão {tv.mostra_estado()}')
                print('Deve ligar primeiro a Televisão')
                print('=' * 100)
            else:
                controlo_remoto.next_channel()
                print('=' * 100)
        if opc == 5:
            estado = tv.mostra_estado()
            if estado == "desligada":
                print(f'Televisão {tv.mostra_estado()}')
                print('Deve ligar primeiro a Televisão')
                print('=' * 100)
            else:
                controlo_remoto.previous_channel()
                print('=' * 100)
        if opc == 6:
            estado = tv.mostra_estado()
            if estado == "desligada":
                print(f'Televisão {tv.mostra_estado()}')
                print('Deve ligar primeiro a Televisão')
                print('=' * 100)
            else:
                controlo_remoto.select_channel()
                print('=' * 100)


menu_tv()
