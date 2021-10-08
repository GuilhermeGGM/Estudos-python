from random import randint
from time import sleep


def sorteio(val):
    print('Sorteando os valoes da lista : ',end='')
    for c in range (1, 7):
        ram = randint(1, 9)
        val.append(ram)
        print(ram, end=' ', flush=True)
        sleep(0.3)
    print('PRONTO')


sort = []
sorteio(sort)
def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            par = c
            soma += par
    print(f'\nSomando os valores pares de {lista}, temos {soma}')


somapar(sort)
