def mergeSort(lista):
    resultado = []
    if len(lista) < 2:
        return lista
    meio = int(len(lista) / 2)
    inicio_meio = mergeSort(lista[:meio])
    meio_fim = mergeSort(lista[meio:])
    contador1 = 0
    contador2 = 0
    while contador1 < len(inicio_meio) and contador2 < len(meio_fim):
            if inicio_meio[contador1] > meio_fim[contador2]:
                resultado.append(meio_fim[contador2])
                contador2 += 1
            else:
                resultado.append(inicio_meio[contador1])
                contador1 += 1
    resultado += inicio_meio[contador1:]
    resultado += meio_fim[contador2:]
    return resultado