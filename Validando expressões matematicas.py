expre = (input('Digite a expressão: '))
#for pe,pd in expre:
if expre.count('(') == expre.count(')'):
    print('A sua expressão está certa')
else:
    print('A sua expressão esta errada')
print(expre.count('('))
print(expre.count(')'))