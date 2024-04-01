
# kreiramo klasu Student 
# svaki student ima ime, matični broj i datum rođenja
# svaki datum ima svojstva: dan, mjesec i godinu 

# prmjer kreiranja objekta: s1 = Student('Vesna', 456777, 16, 9, 1978)




class Student: 

    def __init__(self, ime, mbr, dan, mjesec, godina):
        self.ime = ime 
        self.mbr = mbr 
        self.datum = self.datum(dan, mjesec, godina)

    def ispis(self):
        print(self.ime, self.mbr)

    
    class datum: 
        def __init__(self, dan, mjesec, godina):
            self.dan = dan 
            self.mjesec = mjesec
            self.godina = godina

        def datum_ispis(self):
            print(self.dan, self.mjesec, self.godina)


s1 = Student('Vesna', 456777, 16, 9, 1978)

s1.datum.datum_ispis()



