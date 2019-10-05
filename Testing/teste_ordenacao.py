from ordenacao.BubbleSort import bubbleSort
from ordenacao.heapSort import heapsort
from ordenacao.insertShort import insertShort

lista = [3, 1, 87, 31, 4, 90, 23, 77, 2]
while True:
    print("1 - Bubblesort: ")
    print("2 - Heapsort: ")
    print("3 - Insertsort: ")
    escolha  = input("Escolha o método de ordenação desejado: ")
    if int(escolha) == 1:
        print(bubbleSort(lista))
    elif int(escolha) == 2:
        print(heapsort(lista))
    elif int(escolha) == 3:
        print(insertShort(lista))