
r1 = int(input('Tamanho primero lado: '))
r2 = int(input('Tamanho segundo lado: '))
r3 = int(input('Tamanho terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estás retas podem formar um TRIANGULO!')
    if r1 == r2 == r3:
        print('Formam um TRIANGULO EQUILÁTERO!')
    if r1 != r2 != r3 != r1:
        print('Forman um TRIANGULO ESCALENO!')
    else:
        print('formam um TRIANGULO ISÓSCELES!')
else:
    print('Estás retas NÃO podem formar um TRIANGULO!')
