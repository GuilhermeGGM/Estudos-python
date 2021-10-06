print('Quer converter qual temperatura?')
converter = int(input('1 Celsius para Fahrenheit \n2 Fahrenheit para Celsius \n'))
if converter == 1:
    C = float(input('Qual temperatura em Celsius está fazendo? '))
    temp = (C*1.8)+32
    print('A temperatura {}°C convertida em Fahrenheit será de {:.1f}°F '.format(C, temp))
elif converter == 2:
    F = float(input('Qual temperatura em Fahrenheit está fazendo? '))
    temp = (F-32)/1.8
    print('A temperatura {}°F convertida em Celsius será de {:.1f}°C '.format(F, temp))

