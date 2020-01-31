#Crie um programa que leia o nome de uma pessoa e verifique se tem 'SILVA' no nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem SILVA?: {}'.format('SILVA' in nome.upper()))
