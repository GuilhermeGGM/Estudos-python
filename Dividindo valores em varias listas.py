valores = []
par = []
impar = []
while True:
    num = (int(input('Digite um valor: ')))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Você digitou os valores {valores}')
print(f'Os números pares da lista são: {par}')
print(f'E os números ímpares são: {impar}')