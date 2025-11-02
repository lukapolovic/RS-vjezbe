broj1 = float(input("Unesite 1. broj (sa decimalom): "))
broj2 = float(input("Unesite 2. broj (sa decimalom): "))

while True:
        operator = input("Unesite jedan od sljedecih operatora: +, -, *, / : ")
        
        if operator == '+':
            rezultat = broj1 + broj2
        elif operator == '-':
            rezultat = broj1 - broj2
        elif operator == '*':
            rezultat = broj1 * broj2
        elif operator == '/':
            if broj2 == 0:
                print("Dijeljenje s nulom nije dozvoljeno")
                continue
            rezultat = broj1 / broj2
        else:
            print("Unijeli ste krivi operator.")
            continue
        break

print(f"Rezultat operacije {broj1} {operator} {broj2} je {rezultat}")
