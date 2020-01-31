linha = str('\033[1m-' * 50)
print(linha)
print('\033[1mLOJA TOP DEL GUSTA'.center(50))
print(linha)

## COLETANDO VALOR DO PRODUTO E OPÇÃO DE PAGAMENTO

produto = float(input('Informe o preço do produto R$ '))
print('')
print('FORMAS DE PAGAMENTO'.center(50))
print('[1] A vísta Dinheiro com 10% desconto. \n[2] A vísta cartão de crédito com 5% desconto. \n[3] 2x Cartão de crédito sem desconto. \n[4] 3x ou mais no cartão de crédito com juros.')
escolha = int(input('Qual opção deseja? '))
print('')

## GARANTINDO QUE ESCOLHA UMA OPÇÃO VALIDA
while escolha >= 5:
    print('[1] A vísta Dinheiro com 10% desconto. \n[2] A vísta cartão de crédito com 5% desconto. \n[3] 2x Cartão de crédito sem desconto. \n[4] 3x ou mais no cartão de crédito com juros.')
    escolha = int(input('Qual opção deseja? '))
    print('')

## FAZENDO AS CONDIÇOES
## DANDO 10% DE DESCONTO
if escolha == 1:
    pgto = produto - ((produto * 10) / 100)
    linha = str('\033[1m-' * 50)
    print(linha)
    print('\033[1mLOJA TOP DEL GUSTA'.center(50))
    print(linha)
    print('Total a pagar por seu produto sera de R$ {:.2f}'.format(pgto))

## DANDO 5% DE DESCONTO
elif escolha == 2:
    pgto = produto - ((produto * 5) / 100)
    linha = str('\033[1m-' * 50)
    print(linha)
    print('\033[1mLOJA TOP DEL GUSTA'.center(50))
    print(linha)
    print('Total a pagar por seu produto sera de R$ {:.2f}'.format(pgto))

## COBRANDO VALOR NORMAL DO PRODUTO
elif escolha == 3:
    pgto = produto / 2
    linha = str('\033[1m-' * 50)
    print(linha)
    print('\033[1mLOJA TOP DEL GUSTA'.center(50))
    print(linha)
    print('Valor do produto R$ {:.2f} \nParcelado em 2x de R$ {:.2f}'.format(produto, pgto))

## APLICANDO 20% DE JUROS
elif escolha == 4:
    parcelas = int(input('Numero de parcelas: '))
    produto = produto + ((produto * 20) / 100)
    pgto = produto / parcelas
    linha = str('\033[1m-' * 50)
    print(linha)
    print('\033[1mLOJA TOP DEL GUSTA'.center(50))
    print(linha)
    print('Valor do produto com juros R$ {:.2f} \nParcelado em {}x de R$ {:.2f}'.format(produto, parcelas, pgto))