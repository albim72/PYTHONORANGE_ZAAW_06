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


p1 = Osoba("Jan","Nowak",44,99,173)
print(f"kolor oczu: {p1.koloroczu}")
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()} lat")
print(f"czy osoba jest pracownikiem? {p1.czypracownik()}")
print(f"kolor włosów: {p1.kolorwlosow}")

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