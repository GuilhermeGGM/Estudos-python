cont = 0
quant = 0
while cont != 999:
    num = int(input('Digite um valor [Digite 999 para encerrar]: '))
    soma = num
    cont = num
    quant += 1
    if cont > 2 and cont < 999:
        valor = soma + num
print(valor)
print(quant)
