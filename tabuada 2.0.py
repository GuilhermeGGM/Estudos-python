qtab = int(input('Até qual número vc quer ver a tabuada? '))
num = int(input('Quer ver a tabuada de qual numero? '))
print('A tabuada de 1 até {} do número {} é:'.format(qtab, num))
for tab in range(1, qtab+1):
    resul = num*tab
    print('{}x{}={}'.format(num, tab,resul))