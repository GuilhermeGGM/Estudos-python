valor = int(input('Quer contar até quanto?'))
cont = 1
while cont < valor:
    cont+=1
    if cont % 2 == 0:
        print(cont)
