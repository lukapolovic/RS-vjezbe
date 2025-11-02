lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
bez_duplikata = []

def ukloni_duplikate(lista):
    for num in lista:
        if(num in bez_duplikata):
            continue
        else:
            bez_duplikata.append(num)

ukloni_duplikate(lista)
print(bez_duplikata)