times = ('CORINTHIANS', 'PALMEIRAS', 'SANTOS', 'GREMIO', 'CRUZEIRO', 'FLAMENGO', 'VASCO', 'CHAPECOENSE', 'ATLETICO MINEIRO', 'BOTAFOGO', 'ATLETICO PARANAENSE', 'BAHIA', 'SAO PAULO', 'FLUMINENSE', 'SPORT', 'VITORIA', 'CORITIBA', 'AVAI', 'PONTE PRETA', 'ATLETICO GOIANIENSE')

print('=' * 50)
print(f'{'OS TIMES DA SERIE A':^50}')
print('=' * 50)
print()
print(times)
print()
print(f'Os 5 primeiros são: {times[:6]}')
print(f'Os 4 ultimos são: {times[-4:]}')
print()
print(f'Os times na ordem alfabetica: {sorted(times)}')
print()
print(f'O time da CHAPECOENSE está na {times.index('chapecoense'.upper())+1}ª posição')