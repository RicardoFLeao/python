maior = menor = soma = cont = 0
while True:
    num = int(input('digite um numero: '))
    flag = str(input('quer continuar: [s/n] ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if flag == 'N':
        break
media = soma / cont
print(f'Foram digitados {cont} valores, seu total é {soma}, a meida é {media}, o maior é {maior}, o menor é {menor}')
print('fim')
