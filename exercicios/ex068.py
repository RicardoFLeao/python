from random import randint
vitoria = 0

while True:
    computador = randint(1,10)
    jogador = int(input('Digite um valor: '))
    total = computador + jogador
    tipo = input('Você quer PAR ou IMPAR: [P/I]').strip().upper()[0]
    
    while tipo not in ('P', 'I'):
        print('Opção inválida! Digite apenas [P/I]')
        tipo = input('Você quer PAR ou IMPAR: [P/I]').strip().upper()[0]

    print(f'Você jogou {jogador} é o computador jogou {computador}. Total de {total}', end=' ')
    print('deu PAR' if total % 2 ==0 else 'Deu IMPAR')

    if (tipo == 'P' and total % 2 == 0) or (tipo == 'I' and total % 2 == 1):
        print('Você VENCEU!')
        vitoria += 1
    else:
        print('Você PERDEU!')
        break 

print(f'Você ganhou {vitoria} vezes')