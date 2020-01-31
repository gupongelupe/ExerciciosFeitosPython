sexo = str(input('Digite seu sexo: [M/F] ')).upper()
while sexo != 'M' and sexo!= 'F':
    sexo = str(input('Por favor digite novamente [M/F] ')).upper()
    if sexo == 'M':
        print('És macho my amigo!')
    elif sexo == 'F':
        print('És Moça my manita!')