class Osoba:

    koloroczu = "brązowe"

    # opis stanu -> konstruktor klasy
    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolorwlosow = "blond"
        self.info()


    #zachownie  funkcje klasy > metody
    def info(self):
        print("tworzenie nowego obiektu -> Osoba")

    def print_osoba(self):
        print(f"dane osoby -> imię:{self.imie}, nazwisko: {self.nazwisko}, wiek: {self.wiek} lat,"
              f"wzrost: {self.wzrost} cm, waga: {self.waga} kg")

    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False

    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <=25:
            return "waga prawidłowa"
        elif self.bmi() <=30:
            return "nadwaga"
        else:
            return "otyłość"


p1 = Osoba("Jan","Nowak",44,99,173)
print(f"kolor oczu: {p1.koloroczu}")
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {p1.czypracownik()}")
print(f"kolor włosów: {p1.kolorwlosow}")
print(f"bmi ciała wynosi: {p1.bmi():.2f}, opis: {p1.opis_bmi()}")

print("_________________________________________________")

p2 = Osoba("Olga","Kot",27,51,175)
p2.koloroczu = "niebieskie"
print(f"kolor oczu: {p2.koloroczu}")
p2.print_osoba()
print(f"wiek za 10 lat: {p2.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {p2.czypracownik()}")
p2.kolorwlosow = "czarne"
print(f"kolor włosów: {p2.kolorwlosow}")
print("_________________________________________________")

class Pracownik(Osoba):

    # konstruktor z dziedziczeniem
    def __init__(self,imie,nazwisko,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,nazwisko,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie
        self.kolorwlosow = "ciemny blond"

    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko},"
              f"lata pracy: {self.latapracy}, wyngrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True

e1 = Pracownik("Alicja","Kos",34,62,178,"ABC","dyrektor",12,9800)


print(f"kolor oczu: {e1.koloroczu}")
e1.print_osoba()
e1.print_pracownik()
print(f"wiek za 10 lat: {e1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {e1.czypracownik()}")
print(f"kolor włosów: {e1.kolorwlosow}")

print("_________________________________________________")

class Sport:

    def __init__(self,dyscyplina,lataupr,best_wynik):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.best_wynik = best_wynik

    def infosport(self):
        return f"dyscyplina: {self.dyscyplina}, lata uprawiania: {self.lataupr}," \
               f"wynik życiowy: {self.best_wynik}"

class Ekstra:
    pass

class Student(Pracownik,Sport,Ekstra):

    # konstruktor z wielodziedziczeniem
    def __init__(self,imie,nazwisko,wiek,waga,wzrost,idstudenta,kierunek,rokstud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lataupr="",best_wynik=""):
        Pracownik.__init__(self,imie,nazwisko,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lataupr,best_wynik)
        self.idstudenta = idstudenta
        self.kierunek = kierunek
        self.rokstud = rokstud

    def print_student(self):
        print(f"dane studenta -> id: {self.idstudenta}, kierunek: {self.kierunek}, rok studiów: {self.rokstud}")

    def czypracownik(self):
        return self.firma != ""


s1 = Student("Olaf","Kowal",22,77,177,5453,"budowa mostów",2)
s1.print_osoba()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {s1.czypracownik()}")


print("_________________________________________________")

s2 = Student("Olga","Gołąb",23,58,172,75453,"informatyka",3,"XYZ","junior developer",1,3200)
s2.print_osoba()
s2.print_student()
s2.print_pracownik()
print(f"wiek za 10 lat: {s2.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {s2.czypracownik()}")


print("_________________________________________________")

s3 = Student("Pior","Nowik",22,81,183,66534,"filozofia",2,dyscyplina="biegi ultra",lataupr=5,
             best_wynik="102km 18h:45min:12s")

s3.print_osoba()
s3.print_student()
print(s3.infosport())
print(f"wiek za 10 lat: {s3.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {s3.czypracownik()}")
print(f"bmi ciała wynosi: {s3.bmi():.2f}, opis: {s3.opis_bmi()}")

#Stwórz klasę Sportowiec dziedziczącą klasy Osoba i Sport, zbuduj komnstruktor, napisz metodę
# ostatnie_zawody(self,nazwa,wynik,data) -> wypisz dane zawodów
#Stwórz obiekt sport1 (opisujący sportowca) wykorzystaj wszystkie możliwe metody dostępne dla tej instancji

class Sportowiec(Osoba, Sport):
    def __init__(self, imie,nazwisko, wiek, waga, wzrost, dysc, lata, best_wynik):
        Osoba.__init__(self, imie,nazwisko, wiek, waga, wzrost)
        Sport.__init__(self, dysc, lata, best_wynik)

    def ostatnie_zawody(self, nazwa, wynik, data):
        print(f"nazwa zawodów: {nazwa}, data: {data}, wynik: {wynik}")

print("****************************************************************")
sport1 = Sportowiec("Ola", "Kot", 27, 88, 187, "biegi górskie", 10, "35km 5h23min45s")
sport1.print_osoba()
print(f"wiek za 10 lat: {sport1.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {sport1.czypracownik()}")
print(f"bmi ciała wynosi: {sport1.bmi()}, opis: {sport1.opis_bmi()}")
sport1.infosport()
sport1.ostatnie_zawody("Gorce Ultra Trail", "7:45:46", "2021-07-31")