peso = float(input('Qual é o peso do peixe? '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('O peixe tem {}kg a mais do que o permitido '.format(excesso), end='')
    print('então o valor da multa a pagar será de R${:.2f}'.format(multa))
else:
    print('O peixe está dentro do limite de peso, então você não terá que pagar multa.')
