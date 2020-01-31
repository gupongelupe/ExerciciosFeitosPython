tabu = int(input('Que tabuada tu queres? '))
print('')
for c in range(1, 10+1):
    r = (c * tabu)
    print('|{:=2} x {:=2} = {:=3}|'.format(tabu, c, r))