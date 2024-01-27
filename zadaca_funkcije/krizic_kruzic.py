
red_a = [' ', ' ', ' ']
red_b = [' ', ' ', ' ']
red_c = [' ', ' ', ' ']


def krizic(unos): 
    lista = list(unos)
    if lista[0] == 'a':
        red_a.insert(int(lista[1]), 'X')
        return red_a[int(lista[1])]
    elif lista[0] == 'b':
        red_b.insert(int(lista[1]), 'X')
        return red_b[int(lista[1])]
    elif lista[0] == 'c':
        red_b.insert(int(lista[1]), 'X')
        return red_c[int(lista[1])]
    


def kruzic(unos): 
    lista = list(unos)
    if lista[0] == 'a':
        red_a.insert(int(lista[1]), 'O')
        return red_a[int(lista[1])]
    elif lista[0] == 'b':
        red_b.insert(int(lista[1]), 'O')
        return red_b[int(lista[1])]
    elif lista[0] == 'c':
        red_b.insert(int(lista[1]), 'O')
        return red_c[int(lista[1])]



print()
print('  | 0 | 1 | 2 |')
print('---------------')
print('a |   |   |   |')
print('---------------')
print('b |   |   |   |')
print('---------------')
print('c |   |   |   |')
print()







