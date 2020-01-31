from datetime import date
#coletando os dados ..........
print('\33[1m=-\33[m'*20)
nome = str(input('Informe seu nome: ')).strip().capitalize()
nasc = int(input('Em que ano você nasceu? '))
atual = date.today().year
print('\33[1m-=\33[m'*20)
#fazendo as comparaçoes .............
if (atual - nasc) < 18:
    i = 18 - (atual - nasc)
    print('{} em {} ano(s) voce tera que se alistar ao \33[1mSERVICO MILITAR\33[m.'.format(nome, i))
elif (atual - nasc) == 18:
    print('Esta na hora {}, este ano se aliste ao \33[1mSERVIÇO MILITAR\33[m.'.format(nome))
elif (atual - nasc) > 18:
    i = (atual - nasc) - 18
    print('\33[1;31m{} seu tempo de alistamento passou a {} ANO(S), preocure a JUNTA MILITAR de sua cidade urgente para regularizar sua situação.\33[m'.format(nome, i))
