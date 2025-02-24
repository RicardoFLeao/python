print('-'*40)
print(f'{'LOJAO SUPER BARATO':^30}')
print('-'*40)
print()
total = totmil = menor = cont = 0
barato = ''

while True:
    prod = input('Nome do produto: ')
    prec = float(input('Preço do produto: '))
    cont +=1
    total += prec

    if prec > 1000:
        totmil += 1
    
    if cont == 1:
        menor = prec
        barato = prod
    else:
        if prec < menor:
            menor = prec
            barato = prod

    continuar = input('Quer continuar: [S/N]').strip().upper()[0]

    while continuar not in 'SN':
        print('Opção invalida! Digite [S/N]')
        continuar = input('Quer continuar: [S/N]').strip().upper()[0]
    if continuar == 'N':
        print()
        break

print(f'O total da compra é R$ {total:.2f} ')
print(f'Tem {totmil} produtos custando mais de 1000 reais')
print(f'O produto mais barato foi {barato} custando R$ {menor:.2f}')
print('acabou')
