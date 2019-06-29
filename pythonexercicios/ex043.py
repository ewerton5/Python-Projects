p = float(input('Qual é o seu peso? ').strip())
a = float(input('Qual é a sua altura? ').strip())
imc = p/a**2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal!')
elif imc <= 25:
    print('PARABÉNS, você etá na faixa de peso normal!')
elif imc < 30:
    print('Você está em sobrepeso!')
elif imc < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade mórbida, cuidado!')
