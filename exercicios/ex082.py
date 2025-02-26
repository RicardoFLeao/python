lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Você quer continuar: [S/N] ')
    if resp in 'Nn':
        break
print(f'Você digitou os valores: {lista}')
listapar = []
listaimp = []
for valor in lista:
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimp.append(valor)
print(f'Os valores par são: {listapar}')
print(f'Os valores impar são: {listaimp}')
