parni_lista = []
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filtriraj_parne(lista):
    for num in lista:
        if(num % 2 == 0):
            parni_lista.append(num)

filtriraj_parne(lista)
print(parni_lista)

