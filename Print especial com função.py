while True:
    def printe(txt):
        p = len(txt)
        print('=' * (p + 2))
        print(f' {txt}')
        print('=' * (p + 2))


    frase = str(input('Digite algo: '))
    printe(frase)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
