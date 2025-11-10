skladiste = []

class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}")
        print(f"Cijena: {self.cijena} kn")
        print(f"Dostupna kolicina: {self.dostupna_kolicina} kom")

# dodavanje dva proizvoda u skladište
skladiste.append(Proizvod("Mlijeko", 10.5, 50))
skladiste.append(Proizvod("Kruh", 7.0, 30))

# funkcija za dodavanje novog proizvoda u skladište
def dodaj_proizvod(proizvod):
    if isinstance(proizvod, Proizvod):
        skladiste.append(proizvod)
    else:
        print("Greška: argument nije instanca klase Proizvod")
