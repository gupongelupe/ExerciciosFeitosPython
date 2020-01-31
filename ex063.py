print('-=' * 25)
print('SEQUÊNCIA DE FIBONACCI'.center(50))
print('=-' * 25)
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
print('~~' * 25)
print('{} - {}'.format(t1, t2), end='')
c = 2

while n > c:
    n = n-1
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
