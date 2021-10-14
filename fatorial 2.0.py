def contador(num=0, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{f} x {c}', end='/ ')
        f *= c
    return f


print(contador(5, show=True))
