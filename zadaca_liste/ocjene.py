
#4. Kreirajte listu s ocjenama učenika, s tim da najprije se traži unos koliko ima učenika. 
# Zatim Izračunajte i ispišite prosječnu ocjenu razreda, te koliko ima jedinica, a koliko petica.


ucenici = []

broj_ucenika = int(input('Unesite broj učenika: '))


for unos in range(broj_ucenika):
    unos = ucenici.append([input('Unesti ime i prezime učenika: '), int(input('Unesite ocjenu učenika: '))])


ocjene = []

for ucenik in ucenici:
    ocjene.append(ucenik[1])


print(ocjene)


print(f'Prosjecna ocijena je: {sum(ocjene)/broj_ucenika}')

print(f'U razredu ima: {ocjene.count(1)} jedinica.')


print(f'U razredu ima: {ocjene.count(5)} petica.')







