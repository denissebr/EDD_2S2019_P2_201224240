import nodolistabloques
from curses import KEY_RIGHT, KEY_LEFT

class listabloques:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.index = 0#indice actual

    def insertar(self, indice, tiempo, clase, dato, hashanterior, hash1):
        nodo = nodolistabloques.nodolistabloques(indice, tiempo, clase, dato, hashanterior, hash1)
        #print("insertar")
        if self.inicio is None:
         #   print("inicio vacio")
            self.inicio = nodo
            self.fin = nodo
            self.index += 1
        else:
          #  print("entro al else")
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
    
    def estavacia(self):
        if self.inicio is None:
            return True
        return False

    def seleccionarbloque(self, window):
        window.clear()
        window.border(0)
        nodoaux = self.inicio
        while True:
            event = window.getch()

            window.addstr(0, 41, "SELECCIONAR BLOQUE")
            window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
            window.addstr(1, 0, "PRESIONAR ENTER PARA SELECCIONAR EL BLOQUE")

            if self.inicio is not None and nodoaux is not None:
                lugardata = 15
                window.clear()
                window.border(0)
                window.addstr(0, 41, "SELECCIONAR BLOQUE")
                window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                window.addstr(1, 0, "PRESIONAR ENTER PARA SELECCIONAR EL BLOQUE")
                window.addstr(10, 15, "INDEX " + str(nodoaux.getIndex()))
                window.addstr(11, 15, "TIMESTAMP " + str(nodoaux.getTimeStamp()))
                window.addstr(12, 15, "CLASS " + str(nodoaux.getClass()))
                window.addstr(12, 5, "<<")
                window.addstr(12, 93, ">>")
                window.addstr(13, 15, "PREVIOUSHASH " + str(nodoaux.getPreviousHash()))
                window.addstr(14, 15, "HASH " + str(nodoaux.getHash()))
                window.addstr(15, 15, "DATA ")
                indice = 0
                auxdata = ""
                indice1 = 0
                posx = 19
                while indice1 < 50:
                    if nodoaux.getData()[indice] == '\n':
                        #print("Salto", auxdata)
                        lugardata += 1
                        posx = 15
                    else:
                        if nodoaux.getData()[indice] != '\t' and nodoaux.getData()[indice] != '\r' and nodoaux.getData()[indice] != chr(32):
                            window.addstr(lugardata, posx, nodoaux.getData()[indice])
                            indice1 += 1
                            posx += 1
                        else:
                            window.addstr(lugardata, posx, nodoaux.getData()[indice])
                            posx += 1
                            auxdata += nodoaux.getData()[indice]
                         #   print(auxdata)
                    indice += 1
            
            if event == KEY_RIGHT:
                if nodoaux.getSiguiente() is not None:
                    nodoaux = nodoaux.getSiguiente()
            else:
                if event == KEY_LEFT:
                    if nodoaux.getAnterior() is not None:
                        nodoaux = nodoaux.getAnterior()
                else:
                    if event == 459 or event == 10:
                        return nodoaux.getData()
                    else:
                        if event == 27:
                            return None
                
