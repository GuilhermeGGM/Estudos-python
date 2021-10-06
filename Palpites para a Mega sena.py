import random
import time
jogo = [[], [], [], [], [], []]
lista = [[], [], [], [], [], []]
cont = 0
print('-'*31)
print('       JOGO DA AMEGA SENA')
print('-'*31)
numj = int(input('Quantos jogos voce quer que eu sorteie? '))
cont2 = 0
while True:
    for c in range(0, 6):
        sorte = random.randint(1, 60)
        if sorte not in jogo:
            for a in range(0,5):
                jogo[a].append(sorte)
    lista.append(jogo[:])
    jogo.clear()
    cont += 1
    print(f'Jogo {cont}: {lista[cont2]}\n')
    cont2 += 1
    time.sleep(0.7)
    if cont >= numj:
        break