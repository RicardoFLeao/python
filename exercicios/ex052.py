num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[34m', end='')
    print('{}'.format(c), end=' ')
    
print('\n\033[mO número {} tem {} divisores.'.format(num, total))
if total == 2:
    print('O número {} é PRIMO.'.format(num))
else:
    print('O número {} NÃO É PRIMO.'.format(num))
