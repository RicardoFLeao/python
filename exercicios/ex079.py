lista = []
while True:
    num = int(input('digite um valor: '))
    if num not in lista:
        lista.append(num)
        print(f'Valor {num} adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar!')
    
    cont = input('Quer continuar: [S/N] ').strip().upper()[0]
    while cont not in 'SN':
        print('Opção invalida. Digite [S/N] ')
        cont = input('Quer continuar: [S/N] ').strip().upper()[0]
    if cont == 'N':
        break

print(f'Os valores adicionados foram: {lista.sort()}')
