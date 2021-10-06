p = 1
a = int(input('Digite o primeiro termo da PA: '))
pas = int(input('Digite a razão: '))
ter = a
np = 10
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while p <= total:
        print('{} -> '.format(ter), end='')
        ter += pas
        p += 1
    print('Pausa')
    mais = int(input('Digite quantos termos você quer ver a mais (Digite 0 se não quiser ver mais nenhum): '))
print('O programa foi encerrado e mostrou {} termos'.format(total))