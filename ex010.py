dinheiro = float(input('Valor em R$: '))
dolar = dinheiro / 4.08
print('Com R${}, você pode comprar US${:.2f} '.format(dinheiro, dolar))
