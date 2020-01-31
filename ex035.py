t1 = float(input('Digite uma medida: '))
t2 = float(input('Digite uma medida: '))
t3 = float(input('Digite uma medida: '))
m = str('Esses segmentos formam triangulo')
m2 = str('Esses segmentos nao formam triangulo')

if t1 < (t2+t3) and t2 < (t1+t3) and t3 < (t1+t2):
    print(m)
else:
    print(m2)