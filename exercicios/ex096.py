def area(c, l):
   print(f'A área do terreno {c:.2f} x {l:.2f} é: {c * l:.2f}m²')


print(f'Controle de terreno.'.center(25))
print('-' * 25)
comp = float(input('Qual comprimento: '))
larg = float(input('Qual a largura: '))
area(comp, larg)