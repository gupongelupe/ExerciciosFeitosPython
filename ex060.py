from math import factorial
n = int(input('Digite um número: '))
t = factorial(n)
while n != 0:
    print('{}'.format(n),end='')
    print(' x 'if n > 1 else ' = '.format(n), end='')
    n = n - 1
print('{}'.format(t))