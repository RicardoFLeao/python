lista = []
soma = 0
while True:
    pessoa = {
        'nome': str(input('Nome: ')),
        'idade': int(input('Idade: ')),
        'sexo': str(input('Sexo: [F/M] ')).strip().upper()[0]
    }
    while pessoa['sexo'] not in 'FM':
        print('Sexo inválido!', end=' ')
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    soma += pessoa['idade']
    lista.append(pessoa)
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('Opção inválida!', end=' ')
        resp = str(input('Continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\n{lista}')
print(f'\nQuantas pessoas foram cadastradas: {len(lista)}')
media = soma / len(lista)
print(f'A média da idade da pesssoas é: {media}')
mulheres = [p['nome'] for p in lista if p['sexo'] == 'F']
if mulheres:
    print(f'As mulheres cadastradas são: {", ".join(mulheres)}.')
else:
    print('Nenhuma mulher cadastrada!')
acima_media = [p for p in lista if p['idade'] > media]
if acima_media:
    print('Pessoas acima da média de idade:')
    for p in acima_media:
        print(f'  -{p['nome']} ({p['idade']}) anos.')
else:
    print('Ninguem acima da media.')