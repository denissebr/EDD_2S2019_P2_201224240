import nodolistabloques

class listabloques:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.index = 0#indice actual

    def insertar(self, indice, tiempo, clase, dato, hashanterior, hash1):
        nodo = nodolistabloques.nodolistabloques(indice, tiempo, clase, dato, hashanterior, hash1)
        if self.inicio is None:
            self.inicio = nodo
            self.fin = nodo
            self.index += 1
        else:
            self.fin.setSiguiente(nodo)
            nodo.setAnterior(self.fin)
            self.fin = self.fin.getSiguiente()
            self.index += 1

    def getUltimoHash(self):
        if self.inicio is None:
            return 0
        else:
            return self.fin.getHash()

    def getLastIndex(self):
        return self.index