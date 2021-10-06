d = int(input('Insira aquantidade de dias '))
h = int(input('insira a quantidade de horas '))
m = int(input('Insira a quantidade de minutos '))
s = int(input('Insira a quantidade de segundos '))

sd = (d*24)*60*60
sh = h*60*60
sm = m*60
print('{} dias são {} segundos \n{} horas são {} segundos \n{} minutos são {} segundos '.format(d, sd, h, sh, m, sm))