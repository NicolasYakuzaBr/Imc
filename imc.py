print('\nCalcular IMC')

altura = float(input('Informe a sua altura em metros (ex: 1.75): '))
massa = float(input('Informe o seu peso em kg (ex: 70.5): '))

imc = massa / altura**2

print('Seu IMC é: {:.0f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Seu peso está normal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 35:
    print('Você está com obesidade grau I.')
elif imc < 40:
    print('Você está com obesidade grau II.')
else:
    print('Você está com obesidade mórbida (grau III).')

    
