p = float(input('Qual o preço do produto: R$ '))
d = int(input('Qual o desconto aplicado: % '))
t = p - (p*d/100)
print('O produto que custava {:.2f}, na promoção com {}% de desconto, custara R${:.2f}.'.format(p, d, t))
