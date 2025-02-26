print('Progreção aritimetica\n')
prim = int(input('qual o primeiro termo: '))
raz = int(input('qual a razao: '))
print('')
cont = 1
while cont <= 10:
    print(prim, end='→ ')
    prim += raz
    cont +=1
print('fim')