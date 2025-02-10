sal = float(input('Qual o salário do funcionario R$: '))
if sal <= 1250:
    nsal = sal + (sal * 15/100)
else:
    nsal = sal + (sal * 10/100)
print('O funcionario que recebia {:.2f}, agora irá receber {:.2f} de salário.'.format(sal, nsal))
