from random import randint
from time import sleep
comp = randint(0,2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')

print('Escolha sua opção!')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jog = int(input('Qual você escolheu: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 18)
print('Computador jogou {}'.format(itens[comp]))
if jog == 0 or jog == 1 or jog == 2:
    print('Você jogo {}'.format(itens[jog]))
else:
    print('OPÇÃO INVALIDA')
print("-=" * 18)

if comp == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('GANHOU!')
    elif jog == 2:
        print('PERDEU!')

elif comp == 1:
    if jog == 0:
        print('PERDEU!')
    elif jog == 1:
        print('EMPATE!')
    elif jog == 2:
        print('GANHOU!')

elif comp == 2:
    if jog == 0:
        print('GANHOU!')
    elif jog == 1:
        print('PERDEU!')
    elif jog == 2:
        print('EMPATE')
