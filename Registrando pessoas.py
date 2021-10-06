pess = 0
homem = 0
mulherm = 0
while True:
    print('-'*19)
    print('CADASTRE UMA PESSOA')
    print('-'*19)
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        pess += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulherm += 1
    prog = ' '
    while prog not in 'S':
        prog = input('Quer continuar? [S/N] ').strip().upper()[0]
    if prog == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pess}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulherm} com menos de 20 anos')
