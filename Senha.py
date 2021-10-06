usuario = str(input('Digite o seu nome de usuário: '))
senha = str(input('Digite a sua senha: '))
usuario2 = ''
senha2 = ''
while usuario2 != usuario and senha2 != senha:
    print('-='*15)
    usuario2 = str(input('Digite o seu nome de usuário: '))
    senha2 = str(input('Digite a sua senha: '))
    if usuario2 != usuario:
        print('USUÁRIO INVÁLIDO TENTE NOVAMENTE')
    if senha2 != senha:
        print('SENHA INVÁLIDA TENTE NOVAMENTE')
    if senha2 == usuario2:
        print('SENHA INVÁLIDA TENTE NOVAMENTE')
    if usuario2 == senha2:
        print('USUÁRIO INVÁLIDO TENTE NOVAMENTE')
print('Código encerrado'.upper())