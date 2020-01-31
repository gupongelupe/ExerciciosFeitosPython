sal = float(input('Qual o salario do funcionario? '))
novo = sal + (sal * 15 / 100)
print('O salario do funcionario foi de R${:.2f} para R${:.2f}, com 15% de aumento.'.format(sal, novo))
