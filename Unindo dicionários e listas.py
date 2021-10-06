pessoas = {}
mulheres = []
cont = 0
medidade = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: '))
    if sexo == 'F' or sexo == 'f':
        mulheres.append(pessoas["nome"])
    while sexo not in 'Mm' and sexo not in 'Ff':
        sexo = str(input('Sexo: '))
    pessoas['sexo'] = sexo
    pessoas['idade'] = int(input('Idade: '))
    midade = pessoas['idade']
    medidade += midade
    resp = str(input('Que continuar? [S/N] '))
    cont += 1
    if resp in 'Nn':
        break
print(medidade)
medidade = medidade / cont
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {medidade:5.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
