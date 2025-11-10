from shop import proizvodi

narudzbe = []

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_ispis = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {proizvodi_ispis}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(lista_proizvoda):
    if not isinstance(lista_proizvoda, list):
        print("Argument mora biti lista!")
        return
    if not lista_proizvoda:
        print("Lista ne smije biti prazna")
        return
    for p in lista_proizvoda:
        if not isinstance(p, dict):
            print("Svaki element u listi mora biti rječnik")
            return
        if not all(k in p for k in ["naziv", "cijena", "narucena_kolicina"]):
            print("Svaki rječnik mora sadržavati ključeve naziv, cijena i narucena_kolicina!")
            return

    for p in lista_proizvoda:
        proizvod_u_skladistu = next((x for x in proizvodi.skladiste if x.naziv == p["naziv"]), None)
        if not proizvod_u_skladistu or proizvod_u_skladistu.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return

    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in lista_proizvoda)

    nova_narudzba = Narudzba(lista_proizvoda, ukupna_cijena)
    narudzbe.append(nova_narudzba)
    return nova_narudzba
