
red_a = [' ', ' ', ' ']
red_b = [' ', ' ', ' ']
red_c = [' ', ' ', ' ']


def krizic(unos): 
    lista = list(unos)
    if lista[0] == 'a':
        red_a.pop(int(lista[1]))
        red_a.insert(int(lista[1]), 'X')
        return red_a[int(lista[1])]
    elif lista[0] == 'b':
        red_b.pop(int(lista[1]))
        red_b.insert(int(lista[1]), 'X')
        return red_b[int(lista[1])]
    elif lista[0] == 'c':
        red_c.pop(int(lista[1]))
        red_c.insert(int(lista[1]), 'X')
        return red_c[int(lista[1])]
    


def kruzic(unos): 
    lista = list(unos)
    if lista[0] == 'a':
        red_a.pop(int(lista[1]))
        red_a.insert(int(lista[1]), 'O')
        return red_a[int(lista[1])]
    elif lista[0] == 'b':
        red_b.pop(int(lista[1]))
        red_b.insert(int(lista[1]), 'O')
        return red_b[int(lista[1])]
    elif lista[0] == 'c':
        red_c.pop(int(lista[1]))
        red_c.insert(int(lista[1]), 'O')
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

print('Kažite mi tko igra prvi: krizic ili kruzic ?')
prvi_igrac = input('Odgovor: ')

if prvi_igrac == 'krizic':
    krizic(input('Super ! Krizicu molim te unesi svoje prvo polje: '))
elif prvi_igrac == 'kruzic':
    kruzic(input('Super ! Kruzicu molim te unesi svoje prvo polje: '))

print(red_a)
print(red_b)
print(red_c)




