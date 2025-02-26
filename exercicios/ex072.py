extenso =  'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte'
while True:
    
    while True:

        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20: 
            break
        print('Número inválido tente novamente.')

    print(f'Você digitou o número {extenso[num]}')

    continuar = input('Quer continuar: [S/N] ').strip().upper()[0]
        
    while continuar not in 'SN':
        print('Opção inválida. Digite S para sim ou N para não.')
        continuar = input('Quer continuar: [S/N] ').strip().upper()[0]   
    if continuar == 'N':
        break

