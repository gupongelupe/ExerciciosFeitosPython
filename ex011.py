largura = float(input('Digite a largura de sua parede: '))
altura = float(input('Digite a altura de sua parede: '))
area = largura * altura
tinta = area / 2
print('A area de sua parede é de {:.1f}m² \nPara pintala você precisara usar {:.1f} litros de tinta.'.format(area, tinta))
