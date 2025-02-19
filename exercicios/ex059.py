from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while True:
    print('\n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    opcao = int(input('\n>>>>> Qual é a sua opção: '))
    
    if opcao == 1:
        print(f'\nA soma de {n1} + {n2} é {n1 + n2}')
    
    elif opcao == 2:
        print(f'\nO resultado de {n1} * {n2} é {n1 * n2}')
    
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'\nO maior número entre {n1} e {n2} é {maior}')
    
    elif opcao == 4:
        print('\nDigite os números')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    
    elif opcao == 5:
        sleep(1)
        break
    
    else:
        print('Opção Invalida.')
print('Fim do programa. Volte sempre!')