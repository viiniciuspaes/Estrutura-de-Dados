class ListaEncadeada:

   valorOrbital = None
   proximo = None

   def getValorOrbital(self):
      return(self.valorOrbital)

   def getProximo(self):
      return(self.proximo)

   def setValorOrbital(self, valorOrbital):
      self.valorOrbital = valorOrbital

   def setProximo(self, proximo):
      self.proximo = proximo

   def insereInicio(self, raiz, valorOrbital):
      temporario = ListaEncadeada()
      temporario.setProximo(raiz.getProximo())
      temporario.setValorOrbital(valorOrbital)
      raiz.setProximo(temporario)

   def percorreListaEncadeada(self, raiz):
      temporario = raiz.getProximo()
      while(temporario != None):
         print(temporario.getValorOrbital())
         temporario = temporario.getProximo()

   def removeInicio(self, raiz):
      temporario = raiz.getProximo()
      print(temporario.getValorOrbital())
      raiz.setProximo(temporario.getProximo())
      
