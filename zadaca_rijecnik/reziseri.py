
# 1. Iz rječnika 'reziseri':
#   - napravite popis režisera jedan ispod drugog
#   - napišite koji režiser ima najviše, a koji najmanje režiranih filmova




reziseri = {
    'Christopher Nolan': 10,
    'Quentin Tarantino': 9,
    'Martin Scorsese': 25,
    'Steven Spielberg': 34,
    'Stanley Kubrick': 13
}



for reziser in reziseri.keys():
    print(reziser)
    


imena = list(reziseri.keys())
broj = list(reziseri.values())

max_broj = max(broj)
min_broj = min(broj)


index_max = broj.index(max_broj)
index_min = broj.index(min_broj)

print(f'Najviše režiranih ima: {imena[index_max]}')
print(f'Najmanje režiranih ima: {imena[index_min]}')










