print('   .....   MENU   .....   ')
print('Viagens abaixo de 200KM: R$ 0.50 por KM')
print('Viagens acima de 200KM: R$ 0.45 por KM')
d = int(input('Qual a distancia da viagem em KM: '))
if d <= 200:
    total = d * 0.50
else:
    total = d * 0.45
print('\nO total da sua viagem R$ {:.2f}'.format(total))