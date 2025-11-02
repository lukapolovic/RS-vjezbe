lozinka_dobra = False

def provjera_lozinke(lozinka):
    global lozinka_dobra

    duljina_lozinke = len(lozinka)

    sadrzi_veliko_slovo = False
    sadrzi_broj = False
    for character in lozinka:
        if(character.isdigit()):
            sadrzi_broj = True
            continue
        if(character.isupper() == True):
            sadrzi_veliko_slovo = True

    lozinka = lozinka.lower()

    if lozinka == "password" or lozinka == "lozinka":
        print("Lozinka ne smije sadrzavati 'password' ili 'lozinka'")
    elif not sadrzi_veliko_slovo or not sadrzi_broj:
        print("Loinka mora sadrzavati barjem jedno veliko slovo i jedan broj")
    elif not 8 <= duljina_lozinke <= 15:
        print("Lozinka mora sadrzavati izmedu 8 i 15 znakova")
    else:
        print("Lozinka je jaka!")
        lozinka_dobra = True

while not lozinka_dobra:
    lozinka = input("Unesite lozinku: ")
    provjera_lozinke(lozinka)