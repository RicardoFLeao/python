from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['carteira'] = int(input('Carteira de trabalho: (0 não tem)'))

if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Data da contratação: '))
    pessoa['salário'] = float(input('Qual o salário: '))
    pessoa['aposentar'] = ((pessoa['contratação'] + 35) + pessoa['idade']) - datetime.now().year
print()
print('-=' * 20)
print()
for k, v in pessoa.items():
    print(f'  -{k} tem o valor {v}.')
print()

print(pessoa)