## lendo o número
pt = int(input('Digite o valor do Primeiro Termo da P.A: '))
rz = int(input('Digite o valor da Razão da P.A: '))
dc = pt + (10 - 1) * rz

## tentando montar a P.A
for c in range(pt, dc+rz, rz):
    print('{}'.format(c), end=' ')
