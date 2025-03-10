lista = []
pessoa = {}
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while True:
        if pessoa['sexo'] not in 'FM':
            print('Sexo iválido.')
            pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    pessoa.clear()
    resp = input('Cadastrar outra pessoa: [S/N] ').strip().upper()
    while resp not in 'S/N':
        print('Resposta inválida.', end=' ')
        resp = input('Digite S ou N: ').strip().upper()
    if resp == 'N':
        break
print(f'\n{lista}')
print(f'Quantas pessoas foram cadastradas: {len(lista)}')
media = soma / len(lista)
print(f'A media da idade do grupo é: {media}')
print('As mulheres cadastradas são:', end=' ')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}', end=', ')
print(f'\nAs pessoa com idade acima da media são:', end=' ')
for pessoa in lista:
    if pessoa['idade'] > media:
        print(f'{pessoa["nome"]} com ({pessoa["idade"]} anos)', end=', ')
        