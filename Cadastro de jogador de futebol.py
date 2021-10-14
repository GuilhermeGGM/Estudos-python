jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
gols = []
jogador['gols'] = gols
cont = 1
totgols = 0
while True:
    numgols = int(input(f'Quantos gols fez na partida {cont}? '))
    gols.append(numgols)
    totgols += numgols
    jogador['totgols'] = totgols
    cont += 1
    if cont > jogador['partidas']:
        break
print('-='*40)
print(jogador)
print('-='*40)
print(f'O campo "nome" tem o valor {jogador["nome"]}')
print(f'O camp "gols" tem o valor {jogador["gols"]}')
print(f'O campo "totgols" tem o valor {jogador["totgols"]}')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
cont2 = 0
for g in jogador["gols"]:
    cont2 += 1
    print(f'=> Na partida {cont2}, fez {g} gols.')
print(f'Foi um total de {jogador["totgols"]} gols.')
print('-='*40)