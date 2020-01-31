num = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
menor = num
# veficando menor
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
# veficar o maior
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3
print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))
