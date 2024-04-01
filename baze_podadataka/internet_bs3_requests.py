from bs4 import BeautifulSoup
import requests


url = 'https://www.scrapethissite.com/pages/simple/'

podaci = requests.get(url).content

# print(podaci)




sadrzaj = BeautifulSoup(podaci, 'html.parser')
# print(sadrzaj)


podaci_country = sadrzaj.find_all('div', class_="col-md-4")                        
#print(podaci_country)



populacija = sadrzaj.select('.country-population')
lista_p=[p.text for p in populacija]

lista_p = []
for p in populacija:
    lista_p.append(int(p.text))



capital = sadrzaj.select('.country-capital')
lista_c=[c.text for c in capital]

lista_c = []
for c in capital:
    lista_c.append(c.text)



area = sadrzaj.select('.country-area')
lista_a=[a.text for a in area]

lista_a = []
for a in area:
    #print(a)
    lista_a.append(float(a.text))


name = sadrzaj.select('.country-name')
lista_n=[n.text for n in name]

lista_n = []
for n in name:
    #print(a)
    x = n.text
    x = x.strip()
    #print(x)
    lista_n.append(x)
    








