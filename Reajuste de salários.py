salario: float = float(input('Qual o valor do salário atual? R$ '))
if salario <= 280:
    acrescimo = (salario/100)*20
    reajuste = salario + acrescimo
    print('O salário antigo era de R${}, com o acréscimo de 20% no valor de R${}'.format(salario, acrescimo))
    print('O novo salário com o aumento será de R${:.2f}'.format(reajuste))
elif salario <= 700:
    acrescimo = (salario/100)*15
    reajuste = salario + acrescimo
    print('O salário antigo era de R${}, com o acréscimo de 15% no valor de R${}'.format(salario, acrescimo))
    print('O novo salário com o aumento será de R${:.2f}'.format(reajuste))
elif salario <= 1500:
    acrescimo = (salario/100)*10
    reajuste = salario + acrescimo
    print('O salário antigo era de R${}, com o acréscimo de 10% no valor de R${}'.format(salario, acrescimo))
    print('O  novo salário com o aumento será de R${:.2f}'.format(reajuste))
elif salario > 1500:
    acrescimo = (salario/100)*5
    reajuste = salario + acrescimo
    print('O salário antigo era de R${}, com o acréscimo de 5% no valor de R${}'.format(salario, acrescimo))
    print('O novo salário com o aumento será de R${:.2f}'.format(reajuste))
