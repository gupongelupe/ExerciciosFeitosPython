from math import radians, sin, tan, cos
angulo = float(input('Qual angulo você deseja? '))
seno = sin(radians(angulo))
print('')
print('O angulo {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
