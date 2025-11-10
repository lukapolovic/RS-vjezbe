import datetime
import math

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")

dream_car = Automobil("Chevrolet", "Impala", "1969", 30000)
dream_car.ispis()


class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self. b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        return math.sqrt(self.a)

kalkulator = Kalkulator(10, 3)
print("\nZbroj:", kalkulator.zbroj())
print("Oduzimanje:", kalkulator.oduzimanje())
print("Množenje:", kalkulator.mnozenje())
print("Dijeljenje:", kalkulator.dijeljenje())
print("Potenciranje:", kalkulator.potenciranje())
print("Korijen:", kalkulator.korijen())

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
    
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())
print(f"\nNajbolji student je {najbolji_student.ime} sa prosjekom {najbolji_student.prosjek():.2f}")



class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r**2

# Primjer korištenja
krug1 = Krug(25)  # radijus = 5
print(f"\nOpseg kruga: {krug1.opseg():.2f}")
print(f"Povrsina kruga: {krug1.povrsina():.2f}\n")



class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")


class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"{radnik.ime} sada ima placu {radnik.placa}")


radnik1 = Radnik("Luka", "Sofware Developer", 1200)
manager1 = Manager("Zvonimir", "Linijski Manager", 3000, "R&D")

radnik1.work()
manager1.work()

manager1.give_raise(radnik1, 250)
