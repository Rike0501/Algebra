
import random


red_a = [' ', ' ', ' ']
red_b = [' ', ' ', ' ']
red_c = [' ', ' ', ' ']


def krizic(unos): 
    lista = list(unos)
    if lista[0] == 'a':
        red_a.pop(int(lista[1]))
        red_a.insert(int(lista[1]), 'X')
        #return red_a[int(lista[1])]
    elif lista[0] == 'b':
        red_b.pop(int(lista[1]))
        red_b.insert(int(lista[1]), 'X')
        #return red_b[int(lista[1])]
    elif lista[0] == 'c':
        red_c.pop(int(lista[1]))
        red_c.insert(int(lista[1]), 'X')
        #return red_c[int(lista[1])]
    

def kruzic(unos): 
    lista = list(unos)
    if lista[0] == 'a':
        red_a.pop(int(lista[1]))
        red_a.insert(int(lista[1]), 'O')
        #return red_a[int(lista[1])]
    elif lista[0] == 'b':
        red_b.pop(int(lista[1]))
        red_b.insert(int(lista[1]), 'O')
        #return red_b[int(lista[1])]
    elif lista[0] == 'c':
        red_c.pop(int(lista[1]))
        red_c.insert(int(lista[1]), 'O')
        #return red_c[int(lista[1])]

def ispis_tablice():
    print()
    print('  | 0 | 1 | 2 |')
    print('---------------')
    print(f'a | {red_a[0]} | {red_a[1]} | {red_a[2]} |')
    print('---------------')
    print(f'b | {red_b[0]} | {red_b[1]} | {red_b[2]} |')
    print('---------------')
    print(f'c | {red_c[0]} | {red_c[1]} | {red_c[2]} |')
    print()

def provjera_tablice():
    if   red_a[0] == red_a[1] != ' ' and red_a[1] == red_a[2]:
        return 'pobjeda'
    elif red_b[0] == red_b[1] != ' ' and red_b[1] == red_b[2]:
        return 'pobjeda'
    elif red_c[0] == red_c[1] != ' ' and red_c[1] == red_c[2]:
        return 'pobjeda'
    elif red_a[0] == red_b[0] != ' ' and red_b[0]  == red_c[0]:
        return 'pobjeda'
    elif red_a[1] == red_b[1] != ' ' and red_b[1] == red_c[1]:
        return 'pobjeda'
    elif red_a[2] == red_b[2] != ' ' and red_b[2] == red_c[2]:
        return 'pobjeda'
    elif red_a[0] == red_b[1] != ' ' and red_b[1]  == red_c[2]:
        return 'pobjeda'
    elif red_a[2] == red_b[1] != ' ' and red_b[1] == red_c[0]:
        return 'pobjeda'


def provjera_unosa(unos):
    lista = list(unos)
    vrijednost = globals()['red_' + lista[0]]
    index = int(lista[1])
    if len(lista) == 2 and (lista[0] in ['a', 'b', 'c']) and (lista[1] in ['0', '1', '2']) and vrijednost[index] == ' ':
        return 'True'
    else:
        return 'False'



print()

print('DOBRODOŠLI U IGRU KRIŽIĆ KRUŽIĆ !')


ispis_tablice()


while True:
    print('Kažite mi tko igra prvi: krizic ili kruzic ?')
    print('ili utipkatje riječ nasumicno pa ću ja odrediti. :)')
    prvi_igrac = input('Odgovor: ')
    if prvi_igrac == 'krizic' or prvi_igrac == 'kruzic' :
        break
    elif prvi_igrac == 'nasumicno':
        broj = random.randint(0, 1)
        #print(broj)
        if broj == 1:
            prvi_igrac = 'krizic'
            break
        elif broj == 0:
            prvi_igrac = 'kruzic'
            break
    print('Unijeli ste krivu riječ molim ponovono unesite.')


while True:
    if prvi_igrac == 'krizic':
        unos_krizic = input('Super ! Krizicu molim te unesi svoje prvo polje: ')
        if provjera_unosa(unos_krizic) == 'True':
            krizic(unos_krizic)
            flag = 'krizic'
            break
    elif prvi_igrac == 'kruzic':
        unos_kruzic = input('Super ! Kruzicu molim te unesi svoje prvo polje: ')
        if provjera_unosa(unos_kruzic) == 'True':
            kruzic(unos_kruzic)
            flag = 'kruzic'
            break    
    print('Krivi unos !')

ispis_tablice()


if flag == 'krizic': 
    while True:
        while True:
            print()
            unos_kruzic = input('Sada igra kruzic. Kruzicu molim te unesi svoje polje: ')
            if provjera_unosa(unos_kruzic) == 'True': 
                kruzic(unos_kruzic)
                ispis_tablice()
                break
            print('Krivi unos !')
        if provjera_tablice() == 'pobjeda':
             #ispis_tablice()
                print('Kruzic je pobijedio. Čestitam !')
                break
        while True:
            print()
            unos_krizic = input('Sada igra krizic. Krizicu molim te unesi svoje polje: ')
            if provjera_unosa(unos_krizic) == 'True':
                krizic(unos_krizic)
                ispis_tablice()
                break
            print('Krivi unos !')
        if provjera_tablice() == 'pobjeda':
                #ispis_tablice()
                print('Krizic je pobijedio. Čestitam !')
                break
elif flag == 'kruzic': 
    while True:
        while True: 
            print()
            unos_krizic = input('Sada igra krizic. Krizicu molim te unesi svoje polje: ')
            if provjera_unosa(unos_krizic) == 'True':
                krizic(unos_krizic)
                ispis_tablice()
                break
            print('Krivi unos !')
        if provjera_tablice() == 'pobjeda':
                #ispis_tablice()
                print('Krizic je pobijedio. Čestitam !')
                break
        while True:
            print()
            unos_kruzic = input('Sada igra kruzic. Kruzicu molim te unesi svoje polje: ')
            if provjera_unosa(unos_kruzic) == 'True': 
                kruzic(unos_kruzic)
                ispis_tablice()
                break
            print('Krivi unos !')
        if provjera_tablice() == 'pobjeda':
            #ispis_tablice()
            print('Kruzic je pobijedio. Čestitam !')
            break








