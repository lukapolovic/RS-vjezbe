suma = 0

while(True):
    unos = int(input("Unesite broj: "))
    if(unos == 0):
        break

    suma += unos

print(f"Zbroj svih unesenih brojeva je: {suma}")