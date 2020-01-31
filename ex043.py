## lendo peso e altura
peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Altura? (m) '))
## calculando IMC
imc = peso / (altura ** 2)
## CONDIÇÕES
if imc < 18.5:
    print('\033[1mIMC: {:.1f} \nVocê esta ABAIXO do peso.'.format(imc))
elif imc >= 18.5 and imc < 25.0:
    print('\033[1mIMC: {:.1f} \nSeu peso é IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('\033[1mIMC: {:.1f} \nVocê esta com sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('\033[1mIMC: {:.1f} \nVocê está obeso, se cuide!'.format(imc))
elif imc >= 40:
    print('\033[1mIMC: {:.1f} \n\033[31mObesidade mórbida, PROCURE UM MÉDICO URGENTE!\033[m'.format(imc))



