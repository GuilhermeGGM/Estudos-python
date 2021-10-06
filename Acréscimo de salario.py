s = float(input('Qual é o salário do funcionário? '))
a = float(input('Qual será o valor do aumento? '))
d = (s/100)*a
ns = d+s
print('O novo salário será de {:.2f}'.format(ns))
