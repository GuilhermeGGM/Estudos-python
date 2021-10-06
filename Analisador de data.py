dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
if dia > 30 and mes == 4:
    print('Data inválida')
elif dia > 30 and mes == 6:
    print('Data inválida')
elif dia > 30 and mes == 9:
    print('Data inválida')
elif dia > 30 and  mes == 11:
    print('Data inválida')
elif dia > 28 and mes == 2:
    print('Data inválida')
elif dia > 31:
    print('Data inválida')
elif mes > 12:
    print('data inválida')
else:
    print('Data válida')
