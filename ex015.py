dias = int(input('Quantos dias de aluguel: '))
km = float(input('Quantos KM percorreu: '))
total = ((dias * 60) + (km * 0.15))
print('O total a pagar é de R${:.2f}'.format(total))