n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunta nota do aluno: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua média foi {:.1f} é você está REPROVADO!'.format(m))
elif m >= 5 and m < 7:
    print('Sua média foi {:.1f} é você está DE RECUPERAÇÃO!'.format(m))
elif m >= 7:
    print('Sua média foi {:.1f} é você está APROVADO!'.format(m))
