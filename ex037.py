import math
#coletando os dados
num = int(input('Digite um numero inteiro: '))
escolha = int(input(('\33[1mQual sera a base para conversão?\33[m \n Press \33[1m1\33[m para Binário \n Press \33[1m2\33[m para Hexadecimal \n Press \33[1m3\33[m para todas\n')))
#fazendo a condiçao aninhada
if escolha == 1:
    print('{} em binário é {}'.format(num, bin(num)))
elif escolha == 2:
    print('{} em Hexadecimal é {}'.format(num, hex(num)))
elif escolha == 3:
    print('\33[1m{} em Decimal é {}\nem Hexadecimal é {}\nem binário é {}'.format(num, num, hex(num), bin(num) ))