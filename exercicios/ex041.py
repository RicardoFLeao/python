from datetime import date
nas = int(input('Qual a data de nascimento do atleta: '))
idade = date.today().year - nas
print('O atleta está com {} anos!'.format(idade))
if idade <= 9:
    print('Sua categoria é: MIRIM')
elif idade <= 14:
    print('Sua categoria é: INFANTIL')
elif idade <= 19:
    print('Sua categoria é: JÚNIOR')
elif idade <= 25:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')
