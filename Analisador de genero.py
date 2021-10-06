c = 0
cont = int(input('Quantas pessoas estão previstas para o regisro? '))
while c != cont:
    sexo = input('Digite o seu sexo [M/F]: ')
    sexo = sexo.upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido tente novamente')
    else:
        c += 1
print('acabou')
