print('SEQUÊNCIA DE FIBONACCI'.center(30))
print('~' * 30)
termos = int(input('quantos termos você quer mostrar: '))
atual = 0
prox = 1
tot = 1
cont = 0
while cont <= termos:
    print(atual, end=' → ')
    atual = prox
    prox = tot
    tot = prox + atual
    cont +=1

print('fim')
