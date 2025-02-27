temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input('Digite seu nome:'))
    temp.append(float(input('Qual seu peso: ')))
    
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar: [S/N] ').strip().upper()[0]
    
    while resp not in 'SN':
        print('Opção invalida.')
        resp = input('Quer continuar: [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print()
print(f'-=*' *30)
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O menor peso cadastrado foi {menor:.2f} kg.', end='')
for pes in princ:
    if pes[1] == menor:
        print(f'[{pes[0]}]', end=' ')
print(f'\nO maior peso cadastrado foi {maior:.2f} kg.', end='')
for pes in princ:
    if pes[1] == maior:
        print(f'[{pes[0]}]', end=' ')
