from time import sleep

def cont(i, f, p):
    print('-=' * 20)
    print(f'A contagem de {i} até {f} pulando de {p} em {p}:')

    if p == 0:
        print('O passo não pode ser 0. Alterando para 1')
        p = 1

    if p < 0:
        p *= -1

    if i < f:
        while i <= f:
            print(f'{i} ', end='', flush=True)
            sleep(0.3)
            i += p
        print('FIM!')

    else:
        while i >= f:
            print(f'{i} ', end='', flush=True)
            sleep(0.3)
            i -= p
        print('FIM!')

cont(1, 20, 2)
cont(10, 0, 1)
print('-=' * 20)
print('Agora sua vez de personalizar a contagem. ')
inic = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
cont(inic, fim, passo)
