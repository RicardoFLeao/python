a = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura da parede: '))
m = a * l
t = m / 2
print('Sua parede tem a dimensão de {}x{} e sua area e de {:.2f}m2'.format(a, l, m))
print('Para pinta está parede você gastara {:.3f} litros de tinta '.format(t))
