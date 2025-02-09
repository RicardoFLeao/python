carro = int(input('Qual a velocidade atual do carro? '))
if carro > 80:
    print('MULTADO! Você excedeu o limite máximo de velocidade que e 80km/h ')
    print('Você pagara um amulta de R${:.2f}'.format((carro - 80) * 7))
    
print('Tenha um bom dia! Dirija com seguranca!')
