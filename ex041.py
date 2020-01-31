from datetime import date
#coletando dados

print('\33[1m=='*20)
nome = str(input('Nome do atleta: ')).strip().title()
anoat = int(input('Ano do nascimento do atleta: '))
ano = date.today().year
print('\33[1m==\33[m'*20)

#fazendo as comparaçoes

if (ano - anoat) <= 9:
    print('\33[1m{} \n\33[32mCategoria MIRIM\33[m'.format(nome))
elif (ano - anoat) > 9 and (ano - anoat) <= 14:
    print('\33[1m{} \n\33[32mCategoria INFANTIL\33[m'.format(nome))
elif (ano - anoat) > 14 and (ano - anoat) <= 19:
    print('\33[1m{} \n\33[32mCategoria JUNIOR\33[m'.format(nome))
elif (ano - anoat) > 19 and (ano - anoat) == 20:
    print('\33[1m{} \n\33[32mCategoria SÊNIOR\33[m'.format(nome))
elif (ano - anoat) > 20:
    print('\33[1m{} \n\33[32mCategoria MASTER\33[m'.format(nome))