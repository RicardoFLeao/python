lista = ('lapis', 1.75,
         'caderno', 15.00,
         'prato', 10.50,
         'caneta', 3.50,
         'marca texto', 5.00,
         'borracha', 0.50)
print('~' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('~' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos].upper():.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('~' * 40)