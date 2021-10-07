from time import sleep
def contador(inicio, fim, passo):
    for c in range(inicio, fim+1, passo):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('\n')


contador(1, 10, 1)
contador(10, 0, -2)
i = int(input('Digite o começo do contador: '))
f = int(input('Digite o final: '))
p = int(input('Digite o passo: '))
contador(i, f, p)
