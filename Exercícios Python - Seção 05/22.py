"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para
aposentadoria são.

* Ter pelo menos 65 anos,
* Ou  ter trabalhado pelo menos 30 anos,
* Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""
idade = int(input('Digite sua idade: '))
tempo = int(input('Digite tempo de serviço: '))

if idade >= 65 or tempo >= 30:
    print('Aposentado')
elif idade >= 60 and tempo >= 25:
    print('Aposentado')
else:
    print('Não Aposenta')
