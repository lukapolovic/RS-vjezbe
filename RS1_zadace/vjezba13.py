lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])
print(prvi_i_zadnji(lista))


lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
def maks_i_min(lista):
    max = 0
    min = lista[0]
    for num in lista:
        if num > max:
            max = num
        elif num < min:
            min = num

    return (max, min)
print(maks_i_min(lista))


skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
def presjek(skup_1, skup_2):
    presjek = set()
    for num1 in skup_1:
        if num1 in skup_2:
            presjek.add(num1)

    return presjek
print(presjek(skup_1, skup_2))