def quickSort(lista):
    if len(lista) <= 1:
        return lista
    menor, igual, maior = [], [], []
    pivo = lista[0]
    for x in lista:
        if x < pivo:
            menor.append(x)
        elif x > pivo:
            maior.append(x)
        elif x == pivo:
            igual.append(x)
    return quickSort(menor) + igual + quickSort(maior)
