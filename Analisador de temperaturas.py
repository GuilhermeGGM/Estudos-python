contador = 0
while contador != 0:
    temps = int(input('Digite as temperaturas em °C (Para encerrar digite 0) '))
    temps2 = int(temps)
    contador = contador + 1
media = (temps + temps2)/contador
print(media)
