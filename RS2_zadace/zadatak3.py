import math

# 1. Korsiteci list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50
parni_kvadrati = [x ** 2 for x in range(20, 51) if x % 2 == 0]

print(parni_kvadrati)

# 2. Koristeci list comprehension, izgradite listu duljinu svhi nizova u listi rijeci, ali samo za
# nizove koji sadrže slovo a
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if "a" in rijec]

print(duljine_sa_slovom_a)

# 3. Koristeci list comprehension, izgradite listu rjecnika gdje su kljucevi brojevi od 1 do 10,
# a vrijednosti su kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve
# neka vrijednost bude sam broj
kubovi = [{x : x ** 3 if x % 2 != 0 else x} for x in range(1, 11)]

print(kubovi)

# 4. Koristeci dictionary comprehension, izgradite rjecnik iteriranjem kroz listu brojeva od 50 do 500s
# korakom 50, gdje su kljucevi brojevi, a vrijednosti su korijenih tih brojeva zaokruzeni na 2 decimale
korijeni = { x : round(math.sqrt(x), 2) for x in range(50, 501, 50)}

print(korijeni)

# 5. Koristeci list comprehension, izgradite listu rjecnika gdje su kljucevi prezimena studenata,
# a vrijednosti su zbrojeni bodovi, iz liste studenti
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni_bodovi = [{ x["prezime"] : sum(x["bodovi"])} for x in studenti]

print(zbrojeni_bodovi)

# 6. Koristeci dicitonary comprehension, izgradite rjecnik gdje su kljucevi brojevi od 1 do 10,
# a vrijednosti su liste faktorijela tih brojeva
faktorijeli = { x : [math.factorial(y) for y in range(1, x+1)] for x in range(1, 11)}

print(faktorijeli)