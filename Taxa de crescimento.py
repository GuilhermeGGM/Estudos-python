PaisA = int(input('Digite a quantidade de habitantes do pais A: '))
PaisB = int(input('Digite a quantidade de habitantes do pais B: '))
taxaCresA = float(input('Digite a taxa de crescimento em % por ano do pais A: '))
taxaCresB = float(input('Digite a taxa de cresciment0 em % por ano do pais B: '))
cont = 1
while PaisA < PaisB:
    cont += 1
    popa = PaisA
    popb = PaisB
    PaisA = (PaisA*taxaCresA)/100
    PaisB = (PaisB*taxaCresB)/100
    somaA = PaisA + popa
    somaB = PaisB + popb
    PaisA = int(somaA)
    PaisB = int(somaB)
    print(cont)
    print(PaisA)
    print(PaisB)