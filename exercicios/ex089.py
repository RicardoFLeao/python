lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar: [S/N]').strip().upper()[0]
    while resp not in 'SN':
        print('Opção inválida!')
        resp = input('Quer continuar: [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<15}{"Media":>8}')
print('-=' * 15)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<15}{a[2]:>8.1f}')
while True:
    print('-=' * 20)
    opc = int(input('Mostrar nota do aluno: [999 para parar]'))
    if opc == 999:
        print('FINALIZADO...')
        break
    if opc <= len(lista) -1:
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

