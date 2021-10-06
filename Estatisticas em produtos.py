totcom = 0
tot1000 = 0
prodmenor = 0
cont = 0
nomprod = ''
while True:
    cont += 1
    produto = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    totcom += preco
    if preco > 1000:
        tot1000 += 1
    if cont == 1:
        prodmenor = preco
        nomprod = produto
    if preco < prodmenor:
        nomprod = produto
        prodmenor = preco
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi R${totcom}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomprod} que custa R${prodmenor}')
