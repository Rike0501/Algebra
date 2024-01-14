
# Napravite aplikaciju za prikaz tablice množenja. Korisnik treba moći unijeti do kojeg broja će se
# prikazati tablica.



tablica = {


0  : ['X', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ],
1  : [ 1 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ],
2  : [ 2 , 2, 4, 6, 8, 10,12,14,16,18,20 ],
3  : [ 3 , 3, 6, 9,12, 15,18,21,24,27,30 ],
4  : [ 4 , 4, 8,12,14, 18,22,26,30,34,38 ],
5  : [ 5 , 5,10,15,20, 25,30,35,40,45,50 ],
6  : [ 6 , 6,12,18,24, 30,36,42,48,54,60 ],
7  : [ 7 , 7,14,21,28, 35,42,49,56,63,70 ],
8  : [ 8 , 8,16,24,32, 40,48,56,64,72,80 ],
9  : [ 9 , 9,18,27,36, 45,54,63,72,81,90 ],
10 : [ 10,10,20,30,40, 50,60,70,80,90,100]

}



while True:
    print() 
    unos = input('Unesite broj do kojeg želite da tablica prikazuje: ')
   
    if unos.isdigit() and int(unos) <= 10:
        unos = int(unos) 
        print(f'Unijeli ste broj: {unos}')
        print()
        x = 0
        i = 0
        for x in range(unos+1):
            i = 0
            print(' ', end = ' ')
            while unos >= i:
                print(tablica[x][i], end='  ')
                if x != 0:
                    print('|', end=' ')
                if x == 0:
                    print('  ', end='')
                i += 1
            print()
            print('  --')
            x += 1
        break  
  








