def bubbleSort(lista):
    for numero in range(len(lista)-1, 0, -1):
        for i in range(numero):
            if lista[i]>lista[i+1]:
                temporario = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temporario