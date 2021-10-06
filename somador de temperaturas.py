qtemp = int(input('Quantas temperaturas você quer somar? '))
stemp = 0
maiortemp = 0
menortemp= 0
for cont in range(1, qtemp+1):
    temp = int(input('Digite uma temperatura '))
    stemp += temp
    if temp > maiortemp:
        maiortemp = temp
    elif menortemp < temp:
        menortemp = temp
print('A maior temperarura digitada foi {} e a maior foi {}'.format(menortemp, maiortemp))