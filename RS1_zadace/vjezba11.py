lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def grupiraj_po_paritetu(lista):
    grupirano = {"parni" : [], "neparni" : []}
    for num in lista:
        if(num % 2 == 0):
            grupirano["parni"].append(num)
        else:
            grupirano["neparni"].append(num)
    return grupirano


print(grupiraj_po_paritetu(lista))