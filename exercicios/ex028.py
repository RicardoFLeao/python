from random import randint
from time import sleep

computador = randint(0,5)

print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 18)

jogador = int(input('Em qual número eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer! Eu realmente escolhi o número {}'.format(computador))
else:
    print('Você perdeu! O número que eu pensei foi {} e você escolheu {}'.format(computador, jogador))
