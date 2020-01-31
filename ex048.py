## Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = int(0)
for c in range(1, 501, 2):
    if c % 3 ==0:
        s = s + c
        print(c)
print('A soma dos números ímpares multiplos de 3 é {}'.format(s))