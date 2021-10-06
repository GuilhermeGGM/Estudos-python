p = float(input('Quanto custa o produto?'))
d = int(input('Qual será o desconto aplicado?'))
v = (p/100)*d
vf = p-v
print('O novo valor com do produto com o deconto aplicado será de: {:.2f}'.format(vf))