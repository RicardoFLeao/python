from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
rank = []
print('VALORES SORTEADOS')
for k, v in jogo.items():
    print(f"A {k} tirou o valor {v} no dado.")
    sleep(1)
rank = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('-=' * 15)
print("OS VENCEDORES SÃO".center(30))
for i, v in enumerate(rank):
    print(f"{i+1}º lugar: {v[0]} com {v[1]} pontos")
    sleep(0.5)