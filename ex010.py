rs = float(input('Quanto de dinheiro você tem na carteira?'))
dol = float(input('Qual a cotação do dolar atual?'))
v = rs / dol
print('Com {} reais, você consegue comprar {:.2f} dolares.'.format(rs, v))


