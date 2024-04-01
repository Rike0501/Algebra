'''
1. Kreirajte bazu podataka "filmovi.db" koja sadrži tablicu "filmovi" s poljima "naslov" (tekst), "godina" (broj) i "ocjena" (broj). 
Dodajte tri filma u tablicu (npr. "Titanik", 1997, 9.5; "Prijatelji s povlasticama", 1989, 8.2; "Zvjezdani ratovi: Epizoda IV - Nova nada", 1977, 8.7).

2. Kreirajte program koji korisniku omogućuje dodavanje novih filmova u bazu podataka "filmovi.db". 
Program treba pitati korisnika za unos naslova, godine i ocjene filma te ih spremiti u tablicu "filmovi".

3. Napravite program koji prikazuje sve filmove u bazi podataka "filmovi.db" sortirane po godini. Za svaki film prikažite naslov, godinu i ocjenu.

4. Napravite funkciju "izlistaj_filmove" koja će ispisati sve filmove iz baze podataka, sortirane po godini, a zatim po ocjeni. 
Funkcija treba ispisati naslov, godinu, žanr i ocjenu za svaki film.

5. Napravite funkciju "promijeni_ocjenu" koja će omogućiti korisniku da promijeni ocjenu nekog filma. 
Funkcija treba tražiti unos naslova filma i nove ocjene, a zatim ažurirati bazu podataka.

'''  


import psycopg2


def ubacivanje():
    naziv = input('Unesite naziv filma: ') 
    while True:
        try:
            godina = int(input('Unesite godinu: '))
            break
        except:
            print('Neispravan unos.')
    while True:
        try:
            ocjena = float(input('Unesite ocjenu: '))
            break
        except:
            print('Neispravan unos.')
    
    try:
        global query_insert
        conn = psycopg2.connect(database="filmovi",
                        host="172.28.116.29",
                        user="postgres",
                        password="Test123",
                        port="5432")
        cursor1 = conn.cursor()
        print('Tu sam')
        y = (naziv, godina, ocjena)
        print(y)
        cursor1.execute(query_insert, y)
        conn.commit()
        cursor1.close()

    except: 
        print('Greška pri spajanju na bazu')
    finally:
        conn.close()



def sort_godina():
    global query_select_godina
    try:
        conn = psycopg2.connect(database="filmovi",
                        host="172.28.116.29",
                        user="postgres",
                        password="Test123",
                        port="5432")
        cursor1 = conn.cursor()
        cursor1.execute(query_select_godina)
        lista = cursor1.fetchall()
        print(lista)
        cursor1.close()

    except: 
        print('Greška pri spajanju na bazu')
    finally:
        conn.close()



def sort_godina_ocjena():
    global query_select_ocjenagodina
    try:
        conn = psycopg2.connect(database="filmovi",
                        host="172.28.116.29",
                        user="postgres",
                        password="Test123",
                        port="5432")
        cursor1 = conn.cursor()
        cursor1.execute(query_select_ocjenagodina)
        lista = cursor1.fetchall()
        print(lista)
        cursor1.close()

    except: 
        print('Greška pri spajanju na bazu')
    finally:
        conn.close()


def promijeni_ocjenu():
    while True:
        try:
            naziv_film = input('Unesite naslov filma: ')
            nova_ocjena = float(input('Unesite novu ocjenu: '))
            break
        except:
            print('Neispravan unos.')
    
    query_update = '''
    UPDATE filmovi_tablica 
    SET ocjena = %s
    WHERE naslov = %s
    '''
    try:
        conn = psycopg2.connect(database="filmovi",
                        host="172.28.116.29",
                        user="postgres",
                        password="Test123",
                        port="5432")
        cursor1 = conn.cursor()
        print('spojio se')
        cursor1.execute(query_update, (nova_ocjena, naziv_film))
        conn.commit()
        cursor1.close()

    except: 
        print('Greška pri spajanju na bazu')
    finally:
        conn.close()





query_select_godina = '''  
                    SELECT * 
                    FROM filmovi_tablica 
                    ORDER BY godina

'''


query_select_ocjenagodina = ''' 
                    SELECT *
                    FROM filmovi_tablica
                    ORDER BY godina, ocjena

'''


query_insert = ''' INSERT INTO filmovi_tablica 
                (naslov, godina, ocjena)
                VALUES (%s, %s, %s)

               '''


query_create = '''  CREATE TABLE IF NOT EXISTS filmovi_tablica (
                    sifra serial PRIMARY KEY,
                    naslov VARCHAR(100), 
                    godina INT,
                    ocjena float);   
                '''


conn = psycopg2.connect(database="filmovi",
                        host="172.28.116.29",
                        user="postgres",
                        password="Test123",
                        port="5432")

filmovi = {

    1 : ["Titanik", 1997, 9.5],
    2 : ["Prijatelji s povlasticama", 1989, 8.2],
    3 : ["Zvjezdani ratovi: Epizoda IV - Nova nada", 1977, 8.7]


}





try:


    cursor = conn.cursor()
    #print('Idem...')
    cursor.execute(query_create)
    #print('kreirao tablicu')
    conn.commit()

    

    for x in filmovi.items():
        y = (x[1][0], x[1][1], x[1][2])
        #print(y)
        cursor.execute(query_insert, y)

    print('ubacio sam')

    
    conn.commit()


    cursor.close()



except: 
    print('Greška pri spajanju na bazu')

finally:
    conn.close()


ubacivanje()
sort_godina()


promijeni_ocjenu()








