matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorvalor = somacol = 0
for l in range(0, 3):
    for valor in range(0, 3):
        matriz[l][valor] = int(input(f'digite valor para [{l}][{valor}]:  '))
print('-='*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-='*15)
print(f'A soma dos valores par é: {somapar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma da 3ª coluna é: {somacol}')
# maiorvalor = max(matriz[1])
for c in range(0, 3):
    if c == 0:
        maiorvalor = matriz[1][c]
    elif matriz[1][c]> maiorvalor:
        maiorvalor = matriz[1][c]
print(f'O maior valor da segunda linha é: {maiorvalor}')
