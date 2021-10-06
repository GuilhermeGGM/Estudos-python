km = float(input('Quantos quilometros você rodou com o carro? '))
dias = int(input('Por quantos dias você ficou com o carro? '))
rodado = km*0.15
diasr = dias*60
preço = rodado + diasr
print('O preço a pagar pelo carro é de R${:.2}'.format(preço))

