

# 3. Kreirajte listu cijena nekih proizvoda koju unosi korisnik. Proizvoljno odredite broj članova liste. Izračunajte zatim ukupnu cijenu i prosječnu cijenu svih proizvoda.

'''
5. Zadatak s proizvodima i cijenama proširite na način da ispišete račun oblika: 

olovka:     0.8 eura 
gumica:     0.3 eura
...  
----------------------
ukupno:     4.75 eura

Ispišite još i najveću i najmanju cijenu, te prosječnu cijenu svih proizvoda.
Dodajte na ukupni račun podatak o PDV-u, odnosno kolika je cijena bez PDV-a.

'''



proizvodi = []

for unos in range(3):
    unos = proizvodi.append([input('Unesite ime proizvoda: '), float(input('Unesite cijenu proizvoda: '))])


cijene = []

for proizvod in proizvodi:
    cijene.append(proizvod[1])
    print(f'{proizvod[0]}:    {round(proizvod[1], 2)} eura')  

print('----------------------------')



print(f'Ukupno:    {round(sum(cijene), 2)} eura')
print(f'Prosjecno:    {round(sum(cijene)/len(proizvodi), 2)} eura')
print(f'Najmanja:    {round(min(cijene), 2)} eura')
print(f'Najveca:    {round(max(cijene), 2)} eura')
print(f'Ukupno bez PDV-a:    {round(sum(cijene)-sum(cijene)*0.25, 2)} eura')






