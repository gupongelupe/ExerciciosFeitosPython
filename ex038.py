#rebendo os valores
print('\33[1m=-' * 20)
num1 = int(input('\33[1;33mDigite um valor:\33[m '))
num2 = int(input('\33[1;33mDigite outro valor:\33[m '))
print('\33[1m=-' * 20)
#comparando os valores
if num1 > num2:
    print('O primeiro valor é o maior!')
elif num2 > num1:
    print('O segundo valor é o maior!')
elif num1 == num2:
    print('Não existe numero maior, pois os valores são iguais.')