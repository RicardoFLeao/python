from time import sleep

def maiorvalor(*num):
    print('-=' * 10)
    print(f'Analizando valores.')
    if len(num) == 0 :
        print('Não foi informado nenhum valor')
    else:
        for valor in num:
            print(f'{valor} ',end='', flush=True)
            sleep(0.3)
        print(f'\nForam passados {len(num)}, e o maior valor é: {max(num)}')

maiorvalor(2,6,1,7)
maiorvalor(21,41,123,2,7,8)
maiorvalor(0)
maiorvalor()