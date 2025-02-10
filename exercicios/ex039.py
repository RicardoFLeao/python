from datetime import date
nas = int(input('Em que ano você nasceu? '))
idade = date.today().year - nas
if idade < 18:
    print('Você ainda não tem a idade para se alistar.')
    print('Ainda falta {} anos pra você compretar 18.'.format(18 - idade))
elif idade == 18:
    print('Você está a idade certa para o alistamento.')
else:
    print('Você já passou ta idade de alistamento.')
    print('Você tinha que se alistado a {} anos atrás.'.format(idade - 18))
    