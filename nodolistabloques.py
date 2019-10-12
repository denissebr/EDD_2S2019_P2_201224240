class nodolistabloques:
    def __init__(self, indice, tiempo, clase, dato, hashanterior, hash1):
        self.index = indice
        self.timestamp = tiempo
        self.nombre_clase = clase
        self.data = dato
        self.previoushash = hashanterior
        self.hash_actual = hash1
        self.anterior = None
        self.siguiente = None

    def getIndex(self):
        return self.index
    
    def getTimeStamp(self):
        return self.timestamp

    def getClass(self):
        return self.nombre_clase

    def getData(self):
        return self.data
    
    def getPreviousHash(self):
        return self.previoushash

    def getHash(self):
        return self.hash_actual

    def setAnterior(self, nodo):
        self.anterior = nodo

    def setSiguiente(self, nodo):
        self.siguiente = nodo

    def getAnterior(self):
        return self.anterior

    def getSiguiente(self):
        return self.siguiente