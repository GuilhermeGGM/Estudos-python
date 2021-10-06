valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Número duplicado, não adicionado a lista')
    resp = input('Quer continuar?[S/N] ').upper()
    if resp in 'Nn':
        break
valores.sort()
print(valores)