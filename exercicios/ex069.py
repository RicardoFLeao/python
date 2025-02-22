maior = homem = mulher = cadastro = 0
while True:
    print('-'*30)
    print(f'{'Cadastro de pessoa':^30}')
    print('-'*30)
    print()
    idade = int(input('IDADE: '))
    sexo = input('SEXO: [M/F]').strip().upper()[0]
    while sexo not in ('M', 'F'):
        print('Opção inválida! Digite [M/F]')
        sexo = input('SEXO: [M/F] ').strip().upper()[0]
    if idade >= 18: 
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    cadastro += 1
    cont = input('Quer continuar: [S/N]').strip().upper()[0]
    while cont not in ('S','N'):
        print('Opção inválida! Digite [S/N]')
        cont = input('Quer continuar: [S/N]').strip().upper()[0]
    if cont == 'N':
        print()
        break
print(f'Foram cadastradas {cadastro} pessoas')
print(f'Total de pessoas com mais de 18 anos {maior}')
print(f'São {homem} homens')
print(f'São {mulher} mulheres com menos de 20 anos')