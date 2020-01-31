n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c ==0:
        total += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if total != 2:
    print('\n\033[mO número {} é divisível {} vezes. Não é primo'.format(n, total))
else:
    print('\n\033[mO numero {} é divisível apenas por {} e por 1, portanto é PRIMO!'.format(n, n))