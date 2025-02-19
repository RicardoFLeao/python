from random import randint
computador = randint(0, 10)
print('Sou seu computador... Pensei um número entre 0 e 10.')
print('Tente acertar qual foi? ')
acertou = False
palpite = 0
while acertou == False:
    jogador = int(input('Qual o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maior... Tente novamente: ')
        elif jogador > computador:
            print('Menor... Tente novamente: ')
print(f'Acertou! Você consegui acertar o número com {palpite} tentativas.')
