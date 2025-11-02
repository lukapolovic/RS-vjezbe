
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
frekvencije_rijeci = {}

def frekvencija_rijeci(tekst):
    rijeci = tekst.lower().split()

    for rijec in rijeci:
        rijec = rijec.strip(".,!?;:()\"'")
        if rijec in frekvencije_rijeci:
            frekvencije_rijeci[rijec] += 1
        else:
            frekvencije_rijeci[rijec] = 1

    return frekvencije_rijeci

rezultat = frekvencija_rijeci(tekst)
print(rezultat)
