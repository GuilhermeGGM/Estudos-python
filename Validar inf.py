validador = 0
while validador != 1:
    Nome = str(input('Digite o seu nome: '))
    if len(Nome) < 3:
        print('NOME INVÁLIDO')
    Idade = int(input('Digite a sua idade: '))
    if Idade <= 0 or Idade > 150:
        print('IDADE INVÁLIDA')
    Salario = float(input('Digite o seu salário: '))
    if Salario <= 0:
        print('SALÁRIO INVÁLIDO')
    Sexo = str(input('Digite o seu sexo [M/F]: '))
    if Sexo != 'F' or Sexo != 'S':
        print('SEXO INVÁLIDO')
    EstadoCivil = str(input('Digite o seu estadol civil [C (casado/a), S (solteiro/a), V (viúvo/a) ou D (divorciado/a)]: '))
    if EstadoCivil != 'C' and EstadoCivil != 'S' and EstadoCivil != 'V' and EstadoCivil != 'S':
        print('ESTADO CIVIL INVÁLIDO')
    validador = int(input('Digite 1 para encerrar a operação ou digite 2 para recomeçar a operação: '))
