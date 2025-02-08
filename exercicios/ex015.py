km = int(input('Quanto km foram percorridos: '))
tkm = km * 0.15
d = int(input('Por quantos dias o carro foi alugado: '))
td = d * 60
pg = tkm + td
print('O carro foi alugado por {} dias, com um custo R${} \nAndou {}km, com um custo de R${} \nTotalizando R${} a pagar'.format(d, td, km, tkm, pg))
