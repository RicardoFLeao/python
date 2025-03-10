galera = []
pessoa = {}
soma = 0
# codigo para entrada de dados
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F]').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO. Digite apenas [M/F] ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite apenas [S/N] ')
    if resp == 'N':
        break
print('-=' * 30)
# resultado (listagem dos dados)
print(f'Quantas pessoa foram cadastradas: Foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'A média de idade das pessoas é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ',  end='')
for pess in galera:
    if pess['sexo'] == 'F':
        print(f'{pess["nome"]}', end='; ')
print()
print('Pessoas acima da média de idade: ', end='')
for pess in galera:
    if pess['idade'] > media:
        print(f'{pess["nome"]}', end='; ')