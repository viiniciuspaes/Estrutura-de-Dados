class Fila(object):
    def __init__(self):
        self.dados = []
 
    def enfilera(self, elemento):
        self.dados.append(elemento)
 
    def desenfilera(self):
        return self.dados.pop(0)
 
    def vazia(self):
        return len(self.dados) == 0

