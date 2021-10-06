f = int(input('Digite o número que quer ver o fatorial: '))
for c in range(f, 1, -1):
    fa = f
    fat = fa*(fa-1)
    fato = fa*(fa-2)
    print(fat, fato)