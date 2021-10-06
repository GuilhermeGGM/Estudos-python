valores = []
maior = 0
menor = 0
for c in range(1,6):
    num = int(input('Digite um número: '))
    valores.append(num)
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(valores.index(maior))
print(valores.index(menor))
for i,v in enumerate(valores):
    if v == maior:
        print(i)
for i,v in enumerate(valores):
    if v == menor:
        print(i)
print(f'O maior valor digitado foi {maior} e apareceu nas posições ')
print(f'O menor valor digitado foi {menor} e apareceu nas posições ')