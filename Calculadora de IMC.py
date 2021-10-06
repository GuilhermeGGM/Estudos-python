peso = float(input('Qual o seu peso?(Kg) '))
altura = float(input('Qual a sua altura em metros? Exemplo: 1.70m '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}, portanto, você está abaixo do peso'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é de {:.1f}, portanto, você esta no seu peso ideal'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu IMC é de {:.1f}, portanto, você está com sobrepeso'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é de {:.1f}, portanto, você está com obesidade'.format(imc))
elif imc > 40:
    print('Seu imc é de {:.1f}, portanto, você está com obesidade mórbida'.format(imc))

