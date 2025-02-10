vcasa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o seu salário: '))
tempo = int(input('Em quantos anos você quer pagar:'))
meses = tempo * 12
pres = vcasa / meses
print('Neste prazo o valor da prestação sera R$ {:.2f} \nCom um praso de {} meses'.format(pres, meses))

if pres > sal * 30/100:
    print('Seu emprestimo foi negado! Salário abaixo do necessário!')
else:
    print('Seu emprestimo foi aprovado!')
