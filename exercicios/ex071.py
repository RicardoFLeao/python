print('=' * 50)
print(f'{'BANCO LEÃO':^50}')
print('=' * 50)
print()
valor = int(input('Qual valor do seu saque: R$ '))
ced = 100
totced = 0

while True:
    if valor >= ced:
        valor -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'O total de {totced} cédulas de {ced} R$')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        else:
            ced = 1
        totced = 0
        if valor == 0:
            break

print('VOLTE SEMPRE')


