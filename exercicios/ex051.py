print('=' * 30)
print('PROGREÇÃO ARITIMÉTICA'.center(30))
print('=' * 30)
prim = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = prim + (10 * razao)
for c in range(prim, decimo, razao):
    print(c, end = '- ')
print('fim')