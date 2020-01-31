## Coletei a frase e retirei o espaços entre as letras
frase = str(input('Digite uma frase: ')).upper().split()
junto = ''.join(frase)
##
print(len(junto))