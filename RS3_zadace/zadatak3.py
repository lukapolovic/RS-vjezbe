import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnik):
    print("Dohvacanje imena")
    await asyncio.sleep(3)
    korisnicko_ime = korisnik["korisnicko_ime"]
    korisnicki_mail = korisnik["email"]
    print(f"Korisnik: {korisnicko_ime}, Email: {korisnicki_mail}")

    for k in baza_korisnika:
        if k["korisnicko_ime"] == korisnicko_ime and k["email"] == korisnicki_mail: 
            break
        return f"Korisnik {korisnik} nije pronaden."
    
    return await autorizacija(korisnik, korisnik["lozinka"])

async def autorizacija(korisnik, lozinka):
    print("Autorizacija korisnika...")
    await asyncio.sleep(2)
    
    for loz in baza_lozinka:
        if lozinka == loz["lozinka"]:
            return f"Korisnik {korisnik['korisnicko_ime']} Autorizacija uspjesna."
        return f"Korisnik {korisnik['korisnicko_ime']} Autorizacija neuspjesna."
    


async def main():
    rezultat = await autentifikacija({'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com','lozinka': 'lozinka123'})
    print(rezultat)

asyncio.run(main())