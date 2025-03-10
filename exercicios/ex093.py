jogador = {}
partida = []
jogador['nome'] = str(input('Qual nome do jogador: '))
jogos = int(input(f'Quantos jogos o {jogador["nome"]} jogou: '))
for c in range(jogos):
    partida.append(int(input(f'Quantos gols ele marcou na partida {c+1}: ')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou um total de {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    => na partida {i+1} ele marcou {v} gols.')
print(f'Marcando um total de {jogador["total"]} gols')
