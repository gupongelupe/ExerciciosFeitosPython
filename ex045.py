## MOSTRANDO OPÇÕES E COLETANDO A ESCOLHA

from random import randint
from time import sleep

jogador = str(input('\033[1mDigite seu nome: ')).strip().title()
print('=-' * 25)
print('\033[1mSuas opções:'.center(25))
print('[1] PEDRA \n[2] PAPEL \n[3] TESOURA ')
escolha = int(input('Qual sua escolha? '))
computador = randint(1, 3)
print('-=' * 25)
##GARANTI QUE O JOGADOR ESCOLHA UMA OPÇAO VALIDA!
while escolha >3:
    print('\033[1mSuas opções'.center(25))
    print('[1] PEDRA \n[2] PAPEL \n[3] TESOURA ')
    escolha = int(input('Qual sua escolha? '))

## FAZENDO APARECER NA TELA O JOKENPOH DEVAGAR
print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POH')

## CONDIÇOES PARA JOGADOR ESCOLHE PEDRA
if escolha == 1  and computador == 2:
    print('')
    print('-=' * 20)
    print('Computador escolheu PAPEL \n{} escolheu PEDRA \n\033[31mCOMPUTADOR VENCEU!!!\033[m'.format(jogador))
elif escolha == 1 and computador == 3:
    print('')
    print('Computador escolheu TESOURA \n{} escolheu PEDRA \n\033[32m{} VENCEU!!!\033[m'.format(jogador, jogador))
elif escolha == 1 and computador == 1:
    print('')
    print('Computador escolheu PEDRA \n{} escolheu PEDRA \n O jogo EMPATOU!'.format(jogador))

## CONDIÇOES PARA JOGADOR ESCOLHE PAPEL
elif escolha == 2 and computador == 3:
    print('')
    print('Computador escolheu TESOURA \n{} escolheu PAPEL \n\033[31mComputador VENCEU!!!\033[m'.format(jogador))
elif escolha == 2 and computador == 1:
    print('')
    print('Computador escolheu PEDRA \n{} escolheu TESOURA \n\033[32m{} VENCEU!!!\033[m'.format(jogador, jogador))
elif escolha == 2 and computador == 2:
    print('')
    print('Computador escolheu PEDRA \n{} escolheu PEDRA \n O jogo EMPATOU!'.format(jogador))

## CONDIÇOES PARA JOGADOR ESCOLHE TESOURA
elif escolha == 3 and computador == 1:
    print('')
    print('Computador escolheu PEDRA \n{} escolheu TESOURA \n\033[31mComputador VENCEU!!!\033[m'.format(jogador))
elif escolha == 3 and computador == 2:
    print('')
    print('Computador escolheu PAPEL \n{} escolheu TESOURA \n\033[32m{} VENCEU!!!\033[m'.format(jogador, jogador))
elif escolha == 3 and computador == 3:
    print('')
    print('Computador escolheu TESORA \n{} escolheu TESOURA \nO jogo EMPATOU!'.format(jogador))
