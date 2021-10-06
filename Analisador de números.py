numero = int(input('Qual número você quer analisar? '))
num = str(numero)
print('Esse número têm:')
if numero >= 1000:
    print('{} milhar \n{} centenas \n{} dezenas \n{} unidades'.format(num[0], num[1], num[2], num[3]))
elif numero < 1000 and numero >= 100:
    print('{} centenas \n{} dezenas \n{} unidades'.format(num[0], num[1], num[2]))
elif numero < 100 and numero >= 10:
    print('{} dezenas \n{} unidades'.format(num[0], num[1]))
elif numero < 10 and numero >= 0:
    print('{} unidades'.format(num[0]))
