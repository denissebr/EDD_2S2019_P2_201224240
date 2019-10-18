import nodoarbol

class arbol:
    def __init__(self):
        self.raiz = None
    
    #izquierda = 0
    #derecha = 1
    def insertar(self, carnet, nombre):
        nuevo = nodoarbol.nodoarbol(carnet, nombre)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            if self.Existe(carnet, self.raiz) == False:
                nodopadre = None
                auxnodo = self.raiz
                while auxnodo != None:
                    nodopadre = auxnodo
                    if carnet < auxnodo.getCarnet():
                        auxnodo = auxnodo.getIzquierdo()
                    else:
                        auxnodo = auxnodo.getDerecho()
                if carnet < nodopadre.getCarnet():
                    nodopadre.setIzquierda(nuevo)
                    nuevo.setPadre(nodopadre)
                    self.Equilibrar(nodopadre, 0, True)
                else:
                    nodopadre.setDerecha(nuevo)
                    nuevo.setPadre(nodopadre)
                    self.Equilibrar(nodopadre, 1, True)

    def Existe(self, carnet, auxnodo):
        if auxnodo is not None:
            if auxnodo.getCarnet() > carnet:
                return self.Existe(carnet, auxnodo.getIzquierdo())
            else:
                if auxnodo.getCarnet() < carnet:
                    return self.Existe(carnet, auxnodo.getDerecho())
                else:
                    if auxnodo.getCarnet() == carnet:
                        return True
                    else:
                        return False
        else:
            return False

    def Equilibrar(self, nodo, direccion, nuevo):
        salir = False
        while nodo is not None and salir == False:
            if nuevo == True:
                if direccion == 0:
                    fe = nodo.getFe()
                    fe -= 1
                    nodo.setFe(fe)
                else:
                    fe = nodo.getFe()
                    fe += 1
                    nodo.setFe(fe)
            else:
                if direccion == 0:
                    fe = nodo.getFe()
                    fe += 1
                    nodo.setFe()
                else:
                    fe = nodo.getFe()
                    fe -= 1
                    nodo.setFe(fe)
            
            if nodo.getFe() == 0:
                salir = True
            else:
                if nodo.getFe() == -2:
                    if nodo.getIzquierdo().getFe() == 1:
                        self.RDD(nodo)
                    else:
                        self.RSD(nodo)
                    salir = True
                else:
                    if nodo.getFe() == 2:
                        if nodo.getDerecho().getFe() == -1:
                            self.RDI(nodo)
                        else:
                            self.RSI(nodo)
                        salir = True
            if nodo.getPadre() is not None:
                if nodo.getPadre().getDerecho() == nodo:
                    direccion = 1
                else:
                    direccion = 0
            nodo = nodo.getPadre()

    def RDD(self, nodo):
        padre = nodo.getPadre()
        actual = nodo
        hi = actual.getIzquierdo()
        hdi = hi.getDerecho()
        hidi = hdi.getIzquierdo()
        hidd = hdi.getDerecho()

        if padre is not None:
            if padre.getDerecho() == nodo:
                padre.setDerecha(hdi)
            else:
                padre.setDerecha(hdi)
        else:
            self.raiz = hdi

        hi.setDerecha(hidi)
        actual.setIzquierda(hidd)
        hdi.setIzquierda(hi)
        hdi.setDerecha(actual)

        hdi.setPadre(padre)
        actual.setPadre(hdi)
        hi.setPadre(hdi)
        if hidi is not None:
            hidi.setPadre(hi)
        if hidd is not None:
            hidd.setPadre(actual)

        if hdi.getFe() == -1:
            hi.setFe(0)
            actual.setFe(1)
        else:
            if hdi.getFe() == 0:
                hi.setFe(0)
                actual.setFe(0)
            else:
                hi.setFe(-1)
                actual.setFe(0)
        hdi.setFe(0)

    def RDI(self, nodo):
        padre = nodo.getPadre()
        actual = nodo
        hd = actual.getDerecho()
        hdi = hd.getIzquierdo()
        hdii = hdi.getIzquierdo()
        hdid = hdi.getDerecho()

        if padre is not None:
            if padre.getDerecho() == nodo:
                padre.setDerecha(hdi)
            else:
                padre.setIzquierda(hdi)
        else:
            self.raiz = hdi

        actual.setDerecha(hdii)
        hd.setIzquierda(hdid)
        hdi.setIzquierda(actual)
        hdi.setDerecha(hd)

        hdi.setPadre(padre)
        actual.setPadre(hdi)
        hd.setPadre(hdi)

        if hdii is not None:
            hdii.setPadre(actual)
        if hdid is not None:
            hdid.setPadre(hd)

        if hdi.getFe() == -1:
            actual.setFe(0)
            hd.setFe(1)
        else:
            if hdi.getFe() == 0:
                actual.setFe(0)
                hd.setFe(0)
            else:
                if hdi.getFe() == 1:
                    actual.setFe(-1)
                    hd.setFe(0)

        hdi.setFe(0)

    def RSD(self, nodo):
        padre = nodo.getPadre()
        actual = nodo
        hi = actual.getIzquierdo()
        hid = hi.getDerecho()

        if padre is not None:
            if padre.getDerecho() == actual:
                padre.setDerecha(hi)
            else:
                padre.setIzquierda(hi)
        else:
            self.raiz = hi

        actual.setIzquierda(hid)
        hi.setDerecha(actual)

        actual.setPadre(hi)
        if hid is not None:
            hid.setPadre(actual)
        hi.setPadre(padre)

        actual.setFe(0)
        hi.setFe(0)

    def RSI(self, nodo):
        padre = nodo.getPadre()
        actual = nodo
        hd = actual.getDerecho()
        hdi = hd.getIzquierdo()

        if padre is not None:
            if padre.getDerecho() == nodo:
                padre.setDerecha(hd)
            else:
                padre.setIzquierda(hd)
        else:
            self.raiz = hd

        actual.setDerecha(hdi)
        hd.setIzquierda(actual)

        actual.setPadre(hd)
        if hdi is not None:
            hdi.setPadre(actual)

        hd.setPadre(padre)
        actual.setFe(0)
        hd.setFe(0)        

    def Calcular_Altura_Nodo(self, nodo):
        self.altura = 0
        self.AuxAltura(nodo, 0)
        return self.altura

    def AuxAltura(self, nodo, valor):
        if nodo.getIzquierdo():
            self.AuxAltura(nodo.getIzquierdo(), valor + 1)
        if nodo.getDerecho():
            self.AuxAltura(nodo.getDerecho(), valor + 1)
        if nodo.getIzquierdo() == None and nodo.getDerecho() == None and valor > self.altura:
            self.altura = valor  