matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
cont1 = 0
cont2 = 0
for c in range(0,9):
    num = int(input(f'Digite um valor para [{cont2},{cont1}]: '))
    if num % 2 ==0:
        par = num
        somap = par + num
    if cont1 == 3:
        cont1 -= 3
        cont2 += 1
    matriz[cont2][cont1].append(num)
    cont1 += 1
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(somap)