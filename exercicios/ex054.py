from datetime import date

atual = date.today().year
mai = 0
men = 0

for pess in range(1, 8):
    nasc = int(input('Digite o nascimento da {}ª pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        mai += 1
    else:
        men += 1

print('Temos {} maiores de idade.'.format(mai))
print('Temos {} menores de idade.'.format(men))
