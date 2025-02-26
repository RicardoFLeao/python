listanum = []
for contador in range(5):
    num = int(input(f'Digite um valor para a posição {contador}: '))
    listanum.append(num)

maior = max(listanum)
menor = min(listanum)

print(f'Os números digitados foram: {listanum}')

ind_maior = [indice for indice, valor in enumerate(listanum) if valor == maior]
ind_menor = [indice for indice, valor in enumerate(listanum) if valor == menor]

print(f'O maior número digitado foi: {maior} e apareceu nas posições {ind_maior}')
print(f'O menor número digitado foi: {menor} e apareceu nas posições {ind_menor}')
