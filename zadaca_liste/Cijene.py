

# 3. Kreirajte listu cijena nekih proizvoda koju unosi korisnik. Proizvoljno odredite broj članova liste. Izračunajte zatim ukupnu cijenu i prosječnu cijenu svih proizvoda.



proizvodi = []

for unos in range(3):
    unos = proizvodi.append([input('Unesite ime proizvoda: '), float(input('Unesite cijenu proizvoda: '))])

ukupna_cijena = 0

for proizvod in proizvodi:
    #ukupna_cijena = ukupna_cijena + proizvod[1]
    ukupna_cijena += proizvod[1]

prosjecna_cijena = ukupna_cijena/len(proizvodi)

print(f'Ukupna cijena je: {ukupna_cijena}')
print(f'Prosjecna cijena je: {prosjecna_cijena}')


