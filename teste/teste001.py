from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['carteira'] = int(input('Carteira de trabalho: Se não tem [0] '))
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Ano da contratação: '))
    pessoa['salario'] = float(input('Qual o salário: '))
    pessoa['anoapos'] = (pessoa['contratação'] + 35 )
    pessoa['idadeapos'] = pessoa['anoapos'] - nasc
print('\n' + '-' * 40)
print(f"{'DADOS DO FUNCIONÁRIO':^40}")
print('-' * 40)
for k, v in pessoa.items():
    if k == 'salario':
        print(f'{k.capitalize()}: R$ {v:.2f}')
    else:
        print(f'{k.capitalize()}: {v}')
print('-' * 40)
print('Volte sempre!')
