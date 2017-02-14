def intercalar(lista1,lista2):
    contador1 = 0
    contador2 = 0
    resultante = []
    contador3=0
    while contador1 != len(lista1)  and contador2 != len(lista2):
        resultante.append(lista1[contador3])
        resultante.append(lista2[contador3])
        contador2 += 1
        contador1 += 1
        contador3 += 1
    resultante +=lista1[contador1:]
    resultante +=lista2[contador2:]
    return resultante

