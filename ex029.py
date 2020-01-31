velocidade = float(input('Qual a velocidade do veículo? '))
if velocidade <= 80:
    print('{}KM/h esta dentro do limite da rodovia.'.format(velocidade))
else:
    velocidade = velocidade - 80
    multa = velocidade * 7.00
    print('O LIMITE DA RODOVIA É DE 80KM/h, VOCÊ FOI MULTADO EM R$ {:.2f}'.format(multa))
