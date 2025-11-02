from random import randint

broj_pokusaja = 0
broj_za_pogoditi = randint(1, 100)

while (True):
    unos = int(input("Unesite broj: "))
    broj_pokusaja += 1
    if(unos == broj_za_pogoditi):
        break
    elif(unos > broj_za_pogoditi):
        print("Uneseni broj je veci od broja za pogoditi")
        continue
    elif(unos < broj_za_pogoditi):
        print("Uneseni broj je manji od broja za pogoditi")
        continue

print(f"Bravo, pogodio si u {broj_pokusaja} pokusaja.")