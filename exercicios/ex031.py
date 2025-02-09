distancia = int(input('Qual a distancia da viagem: '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
#preco = distancia * 0.50 if distancia <= 200 else preco = distancia * 0.45 (simplificado)
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print('O preço da viagem será de R${:.2f}'.format(preco))
