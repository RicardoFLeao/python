from random import randint
sort = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os números sorteados foi:')

for num in sort:
    print(f'{num} ',end='')

print(f'\nO menor valor sorteado foi {min(sort)}')
print(f'O maior valor sorteado foi {max(sort)}')