


# 2. Iz rječnika 'ucenici':
#   - izračunajte prosječnu visinu svih učenika
#   - napravite popis u kojem se vidi samo redni broj i ime, npr. 
#             1. Marko Marković
#             2. Iva Ivić
#             ...
#   - ispišite broj učenika i učenica (M i Ž) punom rečenicom npr.
#         U razredu ima 6 učenika i 4 učenice.



ucenici = {
    1 : ['Marko Markić', 'Unska 2, Zagreb', 'M', 1.68],
    2 : ['Ana Anić', 'Krivi put 5, Krapina', 'Ž', 1.55],
    3 : ['Pero Perić', 'Splitska 98, Sinj', 'M', 1.80],
    4 : ['Ivan Ivić', 'Jablanova 3, Sisak', 'M', 1.75],
    5 : ['Stjepan Stjepić', 'Brezova 23, Osijek', 'M', 1.85],
    6 : ['Sara Sarić', 'Otočna 28, Split', 'Ž', 1.61],
    7 : ['Marija Marić', 'Riječna 22, Rijeka', 'Ž', 1.59],
    8 : ['Petra Pertrić', 'Desna 54, Đakovo', 'Ž', 1.68],
    9 : ['Edo Edić', 'Kozuraška 21, Zagreb', 'M', 1.78],
    10 : ['Ante Antić', 'Lijeva 18, Imotski', 'M', 1.80]
}


visine = []

for ucenik in ucenici.values():
    visine.append(ucenik[3])


for index in ucenici.items():
    print(f'{index[0]}. {index[1][0]}')


print()
prosjecna_visina = sum(visine)/len(ucenici)
print(f'Prosiječna visina je: {prosjecna_visina}')


print()
spolovi = []

for spol in ucenici.values():
    spolovi.append(spol[2])


muski = spolovi.count('M')
zenski = spolovi.count('Ž')


print(f'U razredu ima {muski} učenika i {zenski} učenica.')












