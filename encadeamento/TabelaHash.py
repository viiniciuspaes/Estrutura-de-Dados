#from funcHash import *
def funcaoHash(id): # funçao hash
    return id % 10
class NoHash:  # classe no
    funcH = None  # recebe uma funçao hash externa
    listaDeNos = None  # tabela

    def __init__(self, funch, tamanho):
        self.funcH = funch
        self.listaDeNos = [None] * tamanho  # define tamanho da tabela

    def insert(self, no):
        idOriginal = no.getNo()
        idConvertido = self.funcH(idOriginal)  # converte usando funçao hash
        if idConvertido < 0 or idConvertido >= len(self.listaDeNos):  # id convertido fora do range da lista
            print(" Erro!", idConvertido, "chave 'out of range'")
            return
        elif self.listaDeNos[idConvertido] == None:  # espaço vazio insere direto
            self.listaDeNos[idConvertido] = [no]
        else:  # espaço em uso colisao insere na lsita
            self.listaDeNos[idConvertido].append(no)

    def edit(self, no):
        indice = self.funcH(no.getNo())
        if self.listaDeNos[indice] == None:
            return
        else:
            lista = self.listaDeNos[indice]
            for x in lista:
                if x != None and x.getNo() == no.getNo():
                    index = lista.index(x)
                    self.listaDeNos[indice][index] = no

    def search(self, no):
        indice = self.funcH(no.getNo())
        lista = self.listaDeNos[indice]
        for x in lista:
            if x == no:
                return x.getNoValue()

    def delet(self, no):
        indice = self.funcH(no.getNo())
        lista = self.listaDeNos[indice]
        lista.remove(no)