rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni_rjecnik(rjecnik):
    obrnuti = {}
    for kljuc, vrijednost in rjecnik.items():
        obrnuti[vrijednost] = kljuc

    return obrnuti

print(obrni_rjecnik(rjecnik))