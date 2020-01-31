import playsound
nome = str(input('Digite seu nome: ')).upper()
print('Eae {}, curtiu a musica haha!'.format(nome))
if nome == 'YAN':
    playsound.playsound('ex021a.mp3')
else:
    playsound.playsound('ex021.mp3')


