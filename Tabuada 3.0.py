while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for cont in range(1, 10+1):
        tab = num * cont
        print(f'{num}X{cont} = {tab}')
    print('='*15)
print('Processo finalizado')