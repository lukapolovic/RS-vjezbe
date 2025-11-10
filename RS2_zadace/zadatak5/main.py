from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for p in proizvodi_za_dodavanje:
    novi_proizvod = proizvodi.Proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])
    proizvodi.dodaj_proizvod(novi_proizvod)

for proizvod in proizvodi.skladiste:
    proizvod.ispis()
    print("\n")


proizvodi_za_narudzbu = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1},
    {"naziv": "Tipkovnica", "cijena": 200, "narucena_kolicina": 3}
]

nova_narudzba = narudzbe.napravi_narudzbu(proizvodi_za_narudzbu)

nova_narudzba.ispis_narudzbe()
