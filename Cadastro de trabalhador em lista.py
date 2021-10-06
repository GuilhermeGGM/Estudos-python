trab = dict()
trab['nome'] = str(input('Nome: '))
trab['anoNasc'] = int(input('Ano de nascimento: '))
trab['CTPS'] = int(input('Carteira de trabalho (Digite 0 caso não tenha): '))
print('-='*40)
Idade = 2018 - trab['anoNasc']
if trab['CTPS'] == 0:
    print(f'o nome tem o valor {trab["nome"]}')
    print(f'Idade tem o valor {Idade}')
    print(f'ctps tem o valor {trab["CTPS"]}')
else:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salário'] = float(input('Salário: R$'))
    aposentadoria = 2018 - trab['contratação'] + 30
    trab['aposentadoria'] = Idade + aposentadoria
    print(f'o nome tem o valor {trab["nome"]}')
    print(f'Idade tem o valor {Idade}')
    print(f'ctps tem o valor {trab["CTPS"]}')
    print(f'Contratação tem o valor {trab["contratação"]}')
    print(f'Salário tem o valor R${trab["salário"]}')
    print(f'Aposentadoria tem o valor {trab["aposentadoria"]}')
