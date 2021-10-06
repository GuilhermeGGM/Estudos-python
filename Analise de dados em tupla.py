num1 = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))
print(num1.count(9))
if 3 in num1:
        print(num1.index(3)+1)
else:
        print('O valor 3 não foi digitado')
for n in num1:
        if n % 2 == 0:
                print(n, end=' ')

