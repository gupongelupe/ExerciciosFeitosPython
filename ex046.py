import emoji
from time import sleep
print('\033[1m-=' * 20)
print('CONTAGEM REGRESSIVA'.center(40))
print('-=' *20)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('')
print(emoji.emojize("BOOOOOOOOM :fireworks: FELIZ ANO NOVO! :tada: ", use_aliases=True))