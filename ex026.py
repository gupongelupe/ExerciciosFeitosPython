frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeiras letra A aparece na posição {}'.format(frase.find('A') + 1))# +1 para sair da posição 0 e ficar 1 pra melhor entendimento
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A') + 1))
