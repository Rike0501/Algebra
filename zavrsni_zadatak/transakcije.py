
# Program za sada izvršava u konzoli
# Funkcionalnosti:
# • Izbornik
# • Otvaranje računa tvrtke
# • Prikaz stanja računa
# • Prikaz prometa po računu
# • Polog novca na račun
# • Podizanje novca s računa
# • Izlaz iz programa (program se nakon svake akcije vrati na početni izbornik u kojem postoji opcija Izlaz)


import datetime


login_info = {'Erik Bastijanic': '123'}
korisnici_info = {'Erik Bastijanic': ['erik@gmail.com', '098765786']}
racuni_info = {'Erik Bastijanic': [0, '344565466', '232']}
transkacije_info = {}



def otvaranje_rac():
    ime_prezime = input('Unesite ime i prezime: ')
    password = str(input('Unesite lozinku za prijavu u ovu aplikaciju: ')) 
    email = input('Unesite email: ')
    br_mob = input('Unesite broj mobitela: ')
    br_kartice = input('Unesite broj kartice: ')
    dat_isteka = input('Unesite datum isteka kartice: ')
    cvv = input('Unesite CVV kartice: ')
    login_info.setdefault(ime_prezime, password)
    korisnici_info.setdefault(ime_prezime, [email, br_mob])
    racuni_info.setdefault(ime_prezime, [0, br_kartice, dat_isteka, cvv])


def stanje(ime_prezime):
    return racuni_info[ime_prezime][0]




def ispis_izbornika():
    print()
    print('-IZBORNIK-')
    print('0. Izlaz')
    print('1. Otvaranje računa tvrtke')
    print('2. Prikaz stanja računa')
    print('3. Prikaz prometa po računu')
    print('4. Polog novca na račun')
    print('5. Podizanje novca s računa')



def polog(iznos, ime_prezime):
    trenutni = racuni_info[ime_prezime][0]
    novi = float(trenutni) + float(iznos)
    vrijeme = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    transkacije_info.setdefault(vrijeme, [ime_prezime, f'Položeno: početnih ({trenutni} €) + {iznos} € = novi iznos({novi} €)'])
    lista = racuni_info.get(ime_prezime)
    lista.pop(0)
    lista.insert(0, novi)
    racuni_info.setdefault(ime_prezime, lista)
    return iznos



def podizanje(iznos, ime_prezime):
    trenutni = racuni_info[ime_prezime][0]
    novi = float(trenutni) - float(iznos)
    vrijeme = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    transkacije_info.setdefault(vrijeme, [ime_prezime, f'Podignuto: početnih ({trenutni} €) + {iznos} € = novi iznos({novi} €)'])
    lista = racuni_info.get(ime_prezime)
    lista.pop(0)
    lista.insert(0, novi)
    racuni_info.setdefault(ime_prezime, lista)
    return iznos







while True:

    ispis_izbornika()

    print()
    print()
    odabir = input('Unesite broj željene radnje: ')

    if odabir == '1':
        otvaranje_rac()
        print(login_info)
        print(korisnici_info)
        print(racuni_info)
    
    elif odabir == '0':
        print('Hvala na povjerenju. Izlazim iz aplikacije.')
        break
    elif odabir == '2':
        korisnik = input('Unesite ime i prezime: ')
        password = input('Unestie password: ')
        if korisnik in login_info.keys() and login_info.get(korisnik) == str(password):
            #print('Prosao sam uvijet')
            print(f'Stanje računa je: {stanje(korisnik)} €')
    elif odabir == '3':
        korisnik = input('Unesite ime i prezime: ')
        password = input('Unestie password: ')
        if korisnik in login_info.keys() and login_info.get(korisnik) == str(password):
            for i in transkacije_info.keys():
                if transkacije_info[i][0] == korisnik:
                    print(f'{i} -- {transkacije_info[i]}')
    elif odabir == '4':
        korisnik = input('Unesite ime i prezime: ')
        password = input('Unestie password: ')
        if korisnik in login_info.keys() and login_info.get(korisnik) == str(password):
            iznos = float(input('Unesit iznos koji želite položiti: '))
            print(f'Položili ste: {polog(iznos, korisnik)} €.') 
    elif odabir == '5':
        korisnik = input('Unesite ime i prezime: ')
        password = input('Unestie password: ')
        if korisnik in login_info.keys() and login_info.get(korisnik) == str(password):
            iznos = float(input('Unesit iznos koji želite položiti: '))
            print(f'Podigli ste: {podizanje(iznos, korisnik)} €.') 

            












