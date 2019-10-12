import nodolistabloques

class listabloques:
    def __init__(self):
        self.inicio = None
        self.fin = None

    def insertar(self, nodo):
        if self.inicio is None:
            self.inicio = nodo
            self.fin = nodo
        else:
            self.fin.setSiguiente(nodo)
            nodo.setAnterior(self.fin)
            self.fin = self.fin.getSiguiente()
