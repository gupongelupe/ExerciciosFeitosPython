#coletando os dados do 'cliente'
comprador = str(input('Digite seu nome: ')).strip().capitalize()
salario = float(input('Informe seus ganhos mensais R$:'))
casa = float(input('informe o valor da casa R$:'))
anos = int(input('Quantos anos deseja pagar: '))
anos = anos * 12
mensal = casa / anos
salario = (salario * 30) / 100
#fazendo as condiçoes
if mensal < salario:
    print('\33[32mParabéns {}, Seu financiamento foi aprovado!\33[m'.format(comprador))
    print(' Numero de parcelas: {} meses \n Valor da parcela R$:{:.2f}'.format(anos, mensal))
elif mensal > salario:
    print('\33[31mDesculpe {}, seu financiamento foi recusado, exedeu 30% dos seus ganhos.\33[m'.format(comprador))