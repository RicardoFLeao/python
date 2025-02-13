maiorPeso = 0
menorPeso = 0

for contador in range(1, 6):
    peso = float(input('digite o peso da {}ª pessoa: '.format(contador)))
    
    if contador == 1:
        maiorPeso = peso
        menorPeso = peso
    if maiorPeso < peso:
        maiorPeso = peso
    if menorPeso > peso:
        menorPeso = peso

print('O maior peso digitado foi {} kg.'.format(maiorPeso))
print('O menor peso digitado foi {} kg.'.format(menorPeso))
