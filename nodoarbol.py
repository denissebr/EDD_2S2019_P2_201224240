class nodoarbol:
    def __init__(self, auxcarnet, auxnombre):
        self.carnet = auxcarnet
        self.nombre = auxnombre
        self.fe = 0
        self.izquierda = None
        self.derecha = None
        self.padre = None

    def setIzquierda(self, izquierdo):
        self.izquierda = izquierdo
    
    def setDerecha(self, derecho):
        self.derecha = derecho

    def getIzquierdo(self):
        return self.izquierda
    
    def getDerecho(self):
        return self.derecha
    
    def getCarnet(self):
        return self.carnet
    
    def getFe(self):
        return self.fe
    
    def getNombre(self):
        return self.nombre

    def setFe(self, auxfe):
        self.fe = auxfe
    
    def setPadre(self, nodo):
        self.padre = nodo

    def getPadre(self):
        return self.padre