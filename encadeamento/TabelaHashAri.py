#Tabela Hash Criada por Ariana Lima com Contribuiçao minha.

class No:
    def __init__(self, dado):
        self._dado = dado
        self._prox = None
        self._ant = None

    def getdado(self):
        return self._dado

    def getprox(self):
        return self._prox

    def setprox(self, proximo):
        self._prox = proximo

    def getant(self):
        return self._ant

    def setant(self, anterior):
        self._ant = anterior


class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def inVazia(self):
        if (self._inicio == None) and (self._fim == None):
            return True
        else:
            return False

    def inserirnofim(self, dado):
        novono = No(dado)
        if self.inVazia():
            self._inicio = novono
            self._fim = novono
        else:
            self._fim.setprox(novono)
            novono.setant(self._fim)
            self._fim = novono

    def pesquisar(self, dado):
        if self.inVazia():
            return False
        else:
            i = self._inicio
            novono = No(dado)
            while i.getdado() != novono.getdado():
                i = i.getprox()
                if i == None:
                    return False
                    break
            else:
                return i

    def remover(self, dado):
        if self.inVazia():
            return ("Erro lista esta vazia")
        else:
            x = self.pesquisar(dado)
            if x == None:
                return ("Elemento não esta na lista")
            else:
                (x.getprox()).setant(x.getant())
                (x.getant()).setprox(x.getprox())
                x.setprox(None)
                x.setant(None)

    def listar(self):
        if self.inVazia == True:
            print("erro")
        i = self._inicio
        while i != None:
            print(str(i.getdado()))
            i = i.getprox()


def Mod(var1, var2):
    if var1 != 0 and var1 < var2:
        return var1
    elif var1 == 0 or var1 == var2:
        return 0
    elif var1 > var2:
        if var1 - var2 < var2:
            return var1 - var2
        elif var1 - var2 > var2:
            var3 = var1 - var2
            while var3 > var2:
                var3 -= var2
            if var3 == var2:
                return 0
            else:
                return var3


class Tabela_Hash(ListaEncadeada):
    def __init__(self, y):
        self.tamanho = y
        self.lista = ListaEncadeada()

    def Tabela(self):
        while self.tamanho > 0:
            self.tamanho -= 1
            self.lista.inserirnofim(None)

    def inserirNaChave(self, chave, dado):
        novoNo = No(dado)
        if self.lista.pesquisar(None) == chave:
            self.lista[chave] = ListaEncadeada()
            self.lista[chave].inserirnofim(novoNo)
        else:
            self.lista[chave].inserirnofim(novoNo)