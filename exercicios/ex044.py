compra = float(input('Qual o valor do produto: R$ '))
print('')
print('-=-' * 15)
print('        CONDIÇÕES DE PAGAMENTO')
print('-=-' * 15)
print('')
print('''[ 1 ] À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO!
[ 2 ] À VISTA NO CARTÃO: 5% DE DESCONTO!
[ 3 ] ATÉ 2X NO CARTÃO: PRECO FORMAL!
[ 4 ] 3X NO CARTAO OU MAIS: 20% DE JUROS!''')
print('')
cond = int(input('Escolha a forma de pagamento: '))
if cond == 1:
    total = compra - (compra * 10 / 100)
elif cond == 2:
    total = compra - (compra * 5 / 100)
elif cond == 3:
    total = compra
    print('Sua compra sera dividida em 2x de {:.2f}'.format(compra / 2))
elif cond == 4:
    total = compra + (compra * 20 / 100)
    parc = int(input('Em quantas vezes sera dividida a compra: '))
    valpar = total / parc
    print('Sua compra sera divivida em {}X de R${:.2f}'.format(parc, valpar))
else:
    print('opção invalida')
    total = compra
print('O valor da sua compra é R$ {:.2f} e o valor total a pagar é R${:.2f}'.format(compra, total))
