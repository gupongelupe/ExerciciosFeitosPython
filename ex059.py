## Lendo os primeiros numeros
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
e = 0
## MENU
while e != 5:
    e = int(input(' [ 1 ] SOMA\n [ 2 ] MULTIPLICAR\n [ 3 ] MAIOR\n [ 4 ] NOVOS NUMEROS\n [ 5 ] SAIR DO PROGRAMA\n '))
    if e == 1: # Fazendo a soma
        t = n1 + n2
        print('{} + {} = {}'.format(n1, n2, t))
        print('')
    elif e == 2: # Fazendo a multiplicação
        t = n1 * n2
        print('{} x {} = {}'.format(n1, n2, t))
        print('')
    elif e == 3:
         if n1 > n2: # Verificando o maior
            print('{} é maior que {}'.format(n1, n2))
            print('')
         elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
            print('')
    elif e == 4: # Colentando os novos numeros
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        e = int(input(' [ 1 ] SOMA\n [ 2 ] MULTIPLICAR\n [ 3 ] MAIOR\n [ 4 ] NOVOS NUMEROS\n [ 5 ] SAIR DO PROGRAMA\n '))
        if e == 1: # Fazendo a mesma operaçao de cima com os novos numeros coletador na Opção 4
            t = n1 + n2
            print('{} + {} = {}'.format(n1, n2, t))
            print('')
        elif e == 2:
            t = n1 * n2
            print('{} x {} = {}'.format(n1, n2, t))
            print('')
        elif e == 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1, n2))
                print('')
            elif n1 < n2:
                print('{} é maior que {}'.format(n2, n1))
                print('')
