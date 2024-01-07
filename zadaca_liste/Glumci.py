
#2. Kreirajte listu koja čuva podatke o imenima i prezimenima 5 glumica i glumaca, ali tako da imena i prezimena unese korisnik. 
# Nakon unosa liste, ispišite listu tako da svaki element liste bude ispisan u novom redu.

glumci = []


for unos in range (5):
    unos = glumci.append([input('Unesite ime: '), input('Unesite prezime: ')])

#print(glumci)

for glumac in glumci: 
    print(f'{glumac[0]} {glumac[1]}')





