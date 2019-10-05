def insertShort(lista):
    for indice in range(1,len(lista)):
        chave = lista[indice]
        sub = indice
        while sub > 0 and lista[sub-1] > chave:
            lista[sub ] = lista[sub-1]
            sub = sub -1
        lista[sub] = chave
    return lista

