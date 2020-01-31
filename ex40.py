#coletando dados
aluno = str(input('informe seu nome: ')).strip().title()
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
#revisando as medias
if m <= 5:
     print('\33[1;31m{}\nVocê foi reprovado! média: {}'.format(aluno, m))
elif m > 5 and m <= 6.9:
    print('\33[1m{}\nVocê esta de recuperação! média: {}'.format(aluno, m))
elif m >= 7:
    print('\33[1;32m{}\nParabéns você foi aprovado! média: {}'.format(aluno, m))
