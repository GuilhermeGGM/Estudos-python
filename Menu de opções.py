import math
print('MENU DE OPÇÕES')
print('Digite [1] para somar')
print('Digite [2] para multipliar')
print('Digite [3] para saber qual é o maior')
print('Digite [4] para digitar novos numeros')
print('Digite [5] para encerrar o programa'.upper())
print('Digite [6] para dividir')
print('Digite [7] para saber a raiz quadrada')
print('Digite [8] para saber o fatorial de um número')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite digite o segundo valor: '))
escolha = int(input('Digite o que você quer fazer: '))
while escolha != 5:
    print('MENU DE OPÇÕES')
    print('Digite [1] para somar')
    print('Digite [2] para multipliar')
    print('Digite [3] para saber qual é o maior')
    print('Digite [4] para digitar novos numeros')
    print('Digite [5] para encerrar o programa'.upper())
    print('Digite [6] para dividir')
    print('Digite [7] para saber a raiz quadrada')
    print('Digite [8] para saber o fatorial de um numero')
    print('='*30)
    if escolha == 1:
        resultado1 = valor1 + valor2
        print('A soma dos valores é {}'.format(resultado1))
        escolha = int(input('Digite o que você quer fazer agora: '))
        print('='*30)
    elif escolha == 2:
        resultado2 = valor1 * valor2
        print('A multiplicação dos valores é {}'.format(resultado2))
        escolha = int(input('Digite o que você quer fazer agora: '))
        print('='*30)
    elif escolha == 3:
        if valor1 > valor2:
            resultado3 = valor1
            print('O maior valor digitado foi {}'.format(resultado3))
        elif valor2 > valor1:
            resultado3 = valor2
            print('O maior valor digitado foi {}'.format(resultado3))
        escolha = int(input('Digite o que você quer fazer agora: '))
        print('='*30)
    elif escolha == 4:
        valor1 = int(input('Digite o primeiro novo valor: '))
        valor2 = int(input('Digite o segundo novo valor: '))
        escolha = int(input('Digite o que você quer fazer agora: '))
        print('='*30)
    elif escolha == 6:
        resultado4 = valor1 / valor2
        print('O resultado da divisão é de {:.2f}'.format(resultado4))
        escolha = int(input('Digite o que voce quer fazer agora: '))
        print('='*30)
    elif escolha == 7:
        raiz = int(input('Digite um valor para saber a sua raiz quadradra: '))
        resultado5 = math.sqrt(raiz)
        print('A raiz quadrada de {} é {:.2f}'.format(raiz, resultado5))
        escolha = int(input('Digite o que voce quer fazer agora: '))
        print('='*30)
    elif escolha == 8:
        fat = int(input('Digite um numero para saber o seu fatorial: '))
        resultado6 = math.factorial(fat)
        print('O fatorial de {} é {}'.format(fat, resultado6))
        escolha = int(input('Escolha o que voce quer fazer agora: '))
print('='*30)
print('Atividade encerrada'.upper())
