peso = float(input('Qual é seu peso? (kg) '))
altu = float(input('Qual a sua altura? (m) '))
imc = peso / (altu ** 2)
print('O seu índice de IMC é: {:.1f} e você está: '.format(imc), end='')
if imc <= 18.5:
    print('ABAIXO DO PESO!')
elif imc <= 25:
    print('PESO IDEAL!')
elif imc <= 30:
    print('SOBREPESO!')
elif imc <= 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')
