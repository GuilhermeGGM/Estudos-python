lado1 = int(input('Insira o valor do primeiro lado do triâgulo '))
lado2 = int(input('Insra o valor do segundo lado '))
lado3 = int(input('Insira o valor do terceiro lado '))
if lado1 == lado2 and lado2 == lado3:
    print('O triângulo é equilátero')
elif lado1 == lado2 and lado2 != lado3:
    print('O triângulo é isósceles')
elif lado1 != lado2 and lado2 != lado3:
    print('o triângulo é escaleno')
