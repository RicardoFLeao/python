sf = float(input('Qual o salario do funcionário: R$ '))
al = float(input('Qual o percentual de almento: % '))
ns = sf + (sf * al/100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passara a receber R${:.2f} de salário.'.format(sf, al, ns))
