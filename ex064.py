total = n = vezes = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    total += n
    vezes += 1
print(f'Você digitou {vezes:^20} números, e a soma deles é {total}')