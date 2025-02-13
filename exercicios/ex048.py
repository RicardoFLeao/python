soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c  # soma += c
        cont = cont + 1  # cont += 1
print('Foram contados {} vores divisiveis por 3. E a soma destes valores é {}.'.format(cont, soma))
