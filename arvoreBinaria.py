class NoHash:
    def __init__(self,valor):                                   # No ja e iniciado com o chave(id)
        self.valor = valor
        self.anterior = None
        self.proximo = None
        self.pai = None

    # -------------------Gets and Sets--------------------------

    def getValor(self):
        return self.valor
    def getAnterior(self):
        return self.anterior
    def getProximo(self):
        return self.proximo
    def setAnterior(self,no):
        self.anterior = no
    def setProximo(self,no):
        self.proximo = no
    def getPai(self):
        return self.pai
    def setPai(self,no):
        self.pai = no

class ArvoreBin:
    def __init__(self,noRaiz):                                  # Raiz e "setada" junto a arvore
        self.raiz = noRaiz

    # -------------------Facilitadores de Codigo--------------------------

    def getRaiz(self):
        return self.raiz
    def anterior(self):
        return self.raiz.getProximo()
    def proximo(self):
        return self.raiz.getAnterior()

    def inserir(self, no):                                      # inserir e uma funçao recursiva
        if no.getValor() > self.raiz.getValor():
            self.inserirMaior(no)
        elif no.getValor() <= self.raiz.getValor():
            self.inserirMenor(no)
    def inserirMenor(self, no):
        if self.proximo():
            self.proximo().inserir(no)
        else:
            self.raiz.setAnterior(ArvoreBin(no))                # cada no da arvore e na verdade outra arvore
            self.raiz.getAnterior().getRaiz().setPai(self.raiz)
    def inserirMaior(self, no):
        if self.anterior():
            self.anterior().inserir(no)
        else:
            self.raiz.setProximo(ArvoreBin(no))
            self.raiz.getProximo().getRaiz().setPai(self.raiz) #adiciona o pai do no como sendo a raiz do no atual

    # Como cada no e uma arvore posso usar o inserir e forma recursiva pegando sempre a raiz do no atual

    def busca(self, valor):                          #busca tambem e recursiva pensando em cada no como uma arvore
        if valor > self.raiz.getValor():
            if self.anterior():
                return self.anterior().busca(valor)
            else:
                return "No nao existe"
        elif valor < self.raiz.getValor():
            if self.proximo():
                return self.proximo().busca(valor)
            else:
                return "No nao existe"
        else:
            return self.raiz

    def buscaInterativa(self,valor):                            # busca nao recursiva custo menor mas sem graça
        x = self.raiz
        while x != None and valor != x.getValor():
            if valor <x.getValor():
                x= self.proximo()
            else:
                x = self.anterior()
        return x

    def percorrer(self): # vai ate o ultimo no da esquerda e volta de forma recursiva printando o pai e o irmao
        if self.raiz:
            if self.proximo() != None:
                self.proximo().percorrer()
            print(self.raiz.getValor())
            if self.anterior() != None:
                self.anterior().percorrer()

    def percorrerPre(self):
        if self.raiz:
            print(self.raiz.getValor())
            if self.proximo() != None:
                self.proximo().percorrer()
            if self.anterior() != None:
                self.anterior().percorrer()

    def percorrerPos(self):
        if self.proximo() != None:
            self.proximo().percorrer()
        if self.anterior() != None:
            self.anterior().percorrer()
        print(self.raiz.getValor())

    def minimo(self):                                           #No mais a esquerda
        if self.proximo():
            x = self.proximo()
            x = x.minimo()
            return x
        else:
            return

    def maximo(self):                                           # No mais a direita
        if self.anterior():
            x = self.anterior()
            x = x.maximo()
            return x
        else:
            return

    def delete(self,no):                                 # existem 3 situaçoes para rearranjar o ramo deletado
        pai = no.getPai()
        filho_esquerdo = no.getAnterior().getRaiz()
        filho_direito =  no.getProximo().getRaiz()
        if filho_direito == None and filho_esquerdo == None:    # No sem filhos
            if no.getValor() <= pai.getValor():
                pai.setAnterior(None)
                return
            else:
                pai.setProximo(None)
                return
        elif filho_direito == None  and filho_esquerdo != None: # No Possui so um filho
            if no.getValor() <= pai.getValor():
                pai.setAnterior(filho_esquerdo)
                filho_esquerdo.setPai(pai)
                return
            else:
                pai.setProximo(filho_esquerdo)
                filho_esquerdo.setPai(pai)
                return
        elif filho_esquerdo == None and filho_direito != None:
            if no.getValor() <= pai.getValor():
                pai.setAnterior(filho_direito)
                filho_direito.setPai(pai)
                return
            else:
                pai.setProximo(filho_direito)
                filho_direito.setPai(pai)
                return
        elif filho_direito != None and filho_direito != None: # No possui dois filhos, necessita revisao
            if no.getValor() <= pai.getValor():
                pai.setAnterior(filho_direito)
                filho_direito.setPai(pai)
                self.inserir(filho_esquerdo)                    #talvez uma rotaçao seja necessaria
                return
            else:
                pai.setProximo(filho_direito)
                filho_direito.setPai(pai)
                self.inserir(filho_esquerdo)
                return
        else:
            return "No nao existe"
