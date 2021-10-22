"""
As tarifas de certo parque de estacionamento são as seguintes:

* 1 a 2 hora - R$ 1,00 cada
* 3 a 4 hora - R$ 1,40 cada
* 5 hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Desse modo, quem estacionar durante 61 minutos
pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque
e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representa "Dez para a uma da tarde". Pretende-se criar um programa que, lidos pelo teclado os
momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a
partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à de partida,
isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.
"""
cheg = str(input("Digite a hora de chegada \n"))
said = str(input("Digite a hora de saida \n"))

hor, minu = cheg.split(":")
sHor, sMinu = said.split(":")

hor = int(hor)
minu = int(minu)
sHor = int(sHor)
sMinu = int(sMinu)
temM = 0
temH = 0

if hor < sHor:
    temH = (sHor - hor)
    if minu < sMinu:
        temH = temH + 1

elif hor > sHor:
    temH = 24 - (hor - sHor)
    if minu < sMinu:
        temH = temH + 1

elif hor == sHor and minu > sMinu:
    temH = 24

elif hor == sHor and minu == sMinu:
    temH = 1

elif hor == sHor and minu < sMinu:
    temH = 1

if temH < 3:
    print(f"O valor cobrador será de R${temH * 1:.2f}")
elif 2 < temH < 5:
    print(f"O valor cobrador será de R${(2 * 1) + ((temH - 2) * 1.4):.2f}")
else:
    print(f"O valor cobrador será de R${((2 * 1) + (2 * 1.4)) + ((temH - 4) * 2):.2f}")