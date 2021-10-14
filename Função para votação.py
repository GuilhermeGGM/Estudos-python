def voto(nasc):
    idade = 2018 - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    if idade >= 16 and idade < 18 or idade >= 60:
        return f'Com {idade} anos: VOTO OPCIONAL'
    if idade >= 18 and idade < 60:
        return f'com {idade} anos: VOTO OBRIGATÓRIO'


ano = int(input('Em que ano vocẽ nasceu? '))
v = voto(ano)
print(v)