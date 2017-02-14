def heapsort(lista):
  for inicio in range((len(lista)-2)/2, -1, -1):
    passagem(lista, inicio, len(lista) - 1)

  for fim in range(len(lista)-1, 0, -1):
    lista[fim], lista[0] = lista[0], lista[fim]
    passagem(lista, 0, fim - 1)
  return lista

def passagem(lista, inicio, fim):
  raiz = inicio
  while True:
    filho = raiz * 2 + 1
    if filho > fim: break
    if filho + 1 <= fim and lista[filho] < lista[filho + 1]:
      filho += 1
    if lista[raiz] < lista[filho]:
      lista[raiz], lista[filho] = lista[filho], lista[raiz]
      raiz = filho
    else:
      break
