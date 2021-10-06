saque = int(input('Qual o valor que você quer sacar? '))
if saque < 10 or saque > 600:
    print('Saque não disponível')
elif saque >= 100:
    saque50 = int(saque - 100)/50
    saque50 = int(saque50)
    saque = saque - 100
    saque50 = str(saque50)
    saque = str(saque)
    print('O caixa irá disponibilizar: \n{} notas de 100'.format(saque[0]))
    print('{} notas de 50'.format(saque50))
    saque = int(saque)
    saque = saque - 50
    saque = str(saque)
    print('{} notas de 10'.format(saque[1]))
    saque = int(saque)
    saque5 = int(saque - 5)
    saque5 = str(saque5)
    saque = str(saque)
    print('{} notas de 5'.format(saque5))
    print('{} moedas de 1'.format(saque[2]))
elif saque <= 99:
    saque = str(saque)
    print('O caixa irá disponibilizar: \n{} notas de 10 \n{}notas de 2'.format(saque[0], saque[1]))
