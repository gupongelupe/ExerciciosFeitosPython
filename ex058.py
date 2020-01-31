from random import randint
from time import sleep
computador = randint(1, 10) #faço o computador 'PENSAR' no numero
print('-=-' * 20)
print('Tente me vencer, pensarei em um numero de 1 a 10 ...')
print('-=-' * 20)
jogador = int(input('Em que numero estou pensando? ')) #jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(1.5)
c = 1
while jogador != computador:
    if jogador > computador:
        print('MENOS...', end='')
        jogador = int(input('Tente novamente: '))
        print('PROCESSANDO ...')
        sleep(1.5)
        c += 1
    elif jogador < computador:
        print('MAIS...', end='')
        jogador = int(input('Tente novamente: '))
        print('PROCESSANDO ...')
        sleep(1.5)
        c += 1
print('-=' * 20)
print('PARABÉNS! Você ganhou, pensei no {} \nVocê tentou {} vezes'.format(jogador, c))