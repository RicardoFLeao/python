r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas retas FORMÃO um TRIANGULO')
else:
    print('Estas retas NÃO FORMÃO um TRIANGULO')