print('Progreção aritimetica\n')
prim = int(input('qual o primeiro termo: '))
raz = int(input('qual a razao: '))
print('')
cont = 1
total = 10
maisTermos = 1

while maisTermos !=0:
    while cont <= total:
        print(prim, end='→ ')
        prim += raz
        cont +=1
    print('pausa')
    maisTermos = int(input('Mostrar mais quantos termos: '))
    total += maisTermos

print(f'Foram mostrados {total} termos')
print('fim')