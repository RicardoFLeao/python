lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = input('Você quer continuar: [S/N] ').strip().upper()[0]
    while resposta not in 'SN':
        print('Opção invalida.')
        resposta = input('Você quer continuar: [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os elementos digitados são: {lista}')
if 5 in lista:
    print(f'O número 5 foi encontrado nas posições: ', end='')
    for i, valor in enumerate(lista):
        if valor == 5:
            print(i, end=' ')
else:
    print('O número não faz parte da lista')
