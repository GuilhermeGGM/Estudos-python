valores = []
cont = 0
while True:
    num = int(input('Digite um numero: '))
    cont += 1
    valores.append(num)
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        valores.sort(reverse=True)
        break
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não esta na lista')
print(f'Você digitou os valores: {valores}')
print(f'Você digitou {cont} valores')