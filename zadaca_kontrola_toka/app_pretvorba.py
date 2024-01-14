
# Napravite aplikaciju za konverziju (u oba smjera):
# • km u milju – (1 km = 0.6214 milje)
# • °C u °F – (0°C = 32°F) obrnuto 𝑇𝑇(°𝐹𝐹) = 𝑇𝑇(°𝐶𝐶) ∗ (9/5) + 32
# • kg u funtu (pounds) – 1 kg = 2.2046 pounds
# • Litra u US galon – 1l = 0.2642 US gal
# • kW (kilowatt) u ks (horsepoweer ili konjska snaga) – 1 kW = 1.3596




print('Dobro došli u aplikaciju za pretvorbu mjernih jedinica.')
print()

while True:
    jedinica = input('Unesite bez navodnika i malim slovima koji modul za pretvorbu želite "brzina", "temperatura", "masa", "volumen", "horsepoweer" :  ')
    if jedinica == 'brzina' or jedinica == 'temperatura' or jedinica == 'masa' or jedinica == 'volumen' or jedinica == 'horsepoweer':
        break
    else:
        pass


if jedinica == 'brzina': 
    while True:
        smjer = input('Unesite bez navodnika i malim slovima u kojem smjeru želite pretvorbu "km u milje" ili "milje u km".')
        if smjer == 'km u milje':
            while True:
                unos_km = input('Unesite brzinu u km: ')
                if unos_km.isdigit():
                    unos_km = float(unos_km)
                    print(f'{unos_km} u KM je {round(unos_km*0.6214, 2)} miljama')
                    break
                else:
                    pass 

            break
        elif smjer == 'milje u km':
            while True:
                unos_milje = input('Unesite brzinu u miljama: ')
                if unos_milje.isdigit():
                    unos_milje = float(unos_milje)
                    print(f'{unos_milje} u miljama je {round(unos_milje/0.6214, 2)} KM')
                    break
                else:
                    pass 

            break







if jedinica == 'temperatura': 
    while True:
        smjer = input('Unesite bez navodnika i malim slovima u kojem smjeru želite pretvorbu "°C u °F" ili "°F u °C".')
        if smjer == '°C u °F':
            while True:
                unos_km = input('Unesite temperaturu u °C: ')
                if unos_km.isdigit():
                    unos_km = float(unos_km)
                    print(f'{unos_km} u KM je {round(unos_km*0.6214, 2)} miljama')
                    break
                else:
                    pass 

            break
        elif smjer == '°F u °C':
            while True:
                unos_milje = input('Unesite temperaturu u °F: ')
                if unos_milje.isdigit():
                    unos_milje = float(unos_milje)
                    print(f'{unos_milje} u miljama je {round(unos_milje/0.6214, 2)} KM')
                    break
                else:
                    pass 

            break





