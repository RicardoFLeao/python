# print('Digite um número para')
# num = int(input('calcular o seu Fatorial: '))
# f = 1
# while num > 0:
#     print(f'{num}', end=' ')
#     print('x' if num > 1 else '=', end=' ')
#     f *= num
#     num -= 1
# print(f)
print('Digite um número para')
num = int(input('Calcular o seu fatorial: '))
f = 1
for c in range(num, 0, -1):
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
print(f)
    