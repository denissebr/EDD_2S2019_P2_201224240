import pydot
import json
import arbol

class graficar:
    def __init__(self, window):
        self.window = window
        self.arbol = arbol.arbol()
        self.graficar_a = ""

    def graficar_lista(self, lista):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
        if lista.estavacia() == False:
            self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
            self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
            posicioninicial = posx = 35
            auxnombre = ""
            tecla = -1
            while True:
                tecla = self.window.getch()
                if tecla == 27:
                    break
                else:
                    if tecla > 31 and tecla < 127:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                        self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
                        self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
                        self.window.addstr(16, posicioninicial, auxnombre)
                        self.window.addstr(16, posx, chr(tecla))
                        posx += 1
                        auxnombre += chr(tecla)
                    else:
                        if tecla == 8:
                            if posx != posicioninicial:
                                self.window.clear()
                                self.window.border(0)
                                self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                                self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
                                self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
                                auxnombre = auxnombre[:-1]
                                self.window.addstr(16, posicioninicial, auxnombre)
                                posx -= 1
                        else:
                            if (tecla == 459 or tecla == 10) and posicioninicial != posx:
                                break
            
            if len(auxnombre) != 0:
                nodoaux = lista.inicio
                grafica = "digraph{\n"
                grafica += str("node[shape=record];\n")
                control = 0
                while nodoaux:
                    grafica += str("block_" + str(control) + "[label = \"Class = " + str(nodoaux.getClass()) + "\\nTimestamp = " + str(nodoaux.getTimeStamp()) + "\\nPHASH = " + str(nodoaux.getPreviousHash())  + "\\nHASH = " + str(nodoaux.getHash()) + "\"];\n")
                    nodoaux = nodoaux.getSiguiente()
                    control += 1
                
                nodoaux = lista.inicio
                control = 0
                while nodoaux:
                    if nodoaux.getAnterior():
                        grafica += str("block_" + str(control) + "->block_" + str(control - 1) + ";\n")
                    
                    if nodoaux.getSiguiente():
                        grafica += str("block_" + str(control) + "->block_" + str(control + 1) + ";\n")
                    
                    nodoaux = nodoaux.getSiguiente()
                    control += 1
                grafica += str("}")

                grafo = pydot.graph_from_dot_data(grafica)
                (g,) = grafo
                g.write_jpg(auxnombre + ".jpg")
        else:
            self.window.addstr(16, 15, "LA LISTA SE ENCUENTRA VACIA")
            while True:
                event = self.window.getch()
                if event == 27:
                    break

    def graficar_arbol(self, data):
        self.arbol = arbol.arbol()
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
        self.graficar_a = ""
        if data is not None:
            self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
            self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
            posicioninicial = posx = 35
            auxnombre = ""
            tecla = -1
            while True:
                tecla = self.window.getch()
                if tecla == 27:
                    break
                else:
                    if tecla > 31 and tecla < 127:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                        self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
                        self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
                        self.window.addstr(16, posicioninicial, auxnombre)
                        self.window.addstr(16, posx, chr(tecla))
                        posx += 1
                        auxnombre += chr(tecla)
                    else:
                        if tecla == 8:
                            if posx != posicioninicial:
                                self.window.clear()
                                self.window.border(0)
                                self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                                self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
                                self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
                                auxnombre = auxnombre[:-1]
                                self.window.addstr(16, posicioninicial, auxnombre)
                                posx -= 1
                        else:
                            if (tecla == 459 or tecla == 10) and posicioninicial != posx:
                                break
            if posicioninicial != posx:
                self.recorrerjson(data) 
                self.graficar_a = "digraph{\n"
                self.graficar_a += str("node[shape = record];\n")
                self.nodos(self.arbol.raiz, "R")
                self.relacionar(self.arbol.raiz, "R")
                self.graficar_a += str("}")
                grafo = pydot.graph_from_dot_data(self.graficar_a)
                (g,) = grafo
                g.write_jpg(auxnombre + ".jpg")
                return
            #print("es json")
        else:
            self.window.addstr(16, 15, "NO HA SELECCIONADO NINGUN BLOQUE")
            while True:
                event = self.window.getch()
                if event == 27:
                    break
        
    def recorrerjson(self, data_json):
        try:
            json_data = json.loads(data_json)
            #print(data_json)
            for carac in json_data:
             #   print(carac)
                if carac == 'value':
              #      print(json_data['value'])
                    auxval = str(json_data['value']).split("-")
                    carnet = auxval[0]
                    nombre = auxval[1]
                    self.arbol.insertar(carnet, nombre)
                else:
                    if carac == 'left':
                        #print("json", json.dumps(json_data['left']))
                        #print(json.loads(str(json_data['left'])))
                        self.recorrerjson(json.dumps(json_data['left']))
                    else:
                        #print(json_data['right'])
                        self.recorrerjson(json.dumps(json_data['right']))
        except:
            print("execpt")
        

    def nodos(self, nod, nombre):
        if nod is not None:
            auxalt = self.arbol.Calcular_Altura_Nodo(nod)
            self.graficar_a += str("a" + nombre + "[label=\"<f0>|{<f1>Carnet: " + str(nod.getCarnet()) + "\\nNombre: " + str(nod.getNombre()) + "\\nFE: " + str(nod.getFe()) + "\\nAltura" + str(auxalt) + "}|<f2>\"];\n")
            if nod.getIzquierdo() is not None:
                auxnombre = nombre + "I"
                self.nodos(nod.getIzquierdo(), auxnombre)
            if nod.getDerecho() is not None:
                auxnombre = nombre + "D"
                self.nodos(nod.getDerecho(), auxnombre)
        
    def relacionar(self, nod, nombre):
        if nod is not None:
            if nod.getDerecho() is not None:
                self.graficar_a += str("a" + nombre + ":<f2>->a" + nombre + "D:<f1>;\n")
            
            if nod.getIzquierdo() is not None:
                self.graficar_a += str("a" + nombre + ":<f0>->a" + nombre + "I:<f1>;\n")

            if nod.getIzquierdo() is not None:
                auxnombre = nombre + "I"
                self.relacionar(nod.getIzquierdo(), auxnombre)
            
            if nod.getDerecho() is not None:
                auxnombre = nombre + "D"
                self.relacionar(nod.getDerecho(), auxnombre)
    
    def graficar_recorrido_preorden(self, data):
        self.arbol = arbol.arbol()
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
        self.graficar_a = ""
        self.indicenodo = 0
        if data is not None:
            self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
            self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
            posicioninicial = posx = 35
            auxnombre = ""
            tecla = -1
            while True:
                tecla = self.window.getch()
                if tecla == 27:
                    break
                else:
                    if tecla > 31 and tecla < 127:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                        self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
                        self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
                        self.window.addstr(16, posicioninicial, auxnombre)
                        self.window.addstr(16, posx, chr(tecla))
                        posx += 1
                        auxnombre += chr(tecla)
                    else:
                        if tecla == 8:
                            if posx != posicioninicial:
                                self.window.clear()
                                self.window.border(0)
                                self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                                self.window.addstr(16, 15, "NOMBRE DEL REPORTE:")
                                self.window.addstr(17, 15, "PRESIONAR ENTER PARA GENERAR REPORTE")
                                auxnombre = auxnombre[:-1]
                                self.window.addstr(16, posicioninicial, auxnombre)
                                posx -= 1
                        else:
                            if (tecla == 459 or tecla == 10) and posicioninicial != posx:
                                break
            
            if posicioninicial != posx:
                self.recorrerjson(data)
                self.graficar_a = "digraph{\n"
                self.graficar_a += str("node[shape = record];\n")
                self.aux_preorden(self.arbol.raiz, "R")
                self.graficar_a += str("}")
                grafo = pydot.graph_from_dot_data(self.graficar_a)
                (g,) = grafo
                g.write_jpg(auxnombre + ".jpg")

    def aux_preorden(self, nodo, nombre):
        if nodo is not None:
            self.graficar_a += str("a_" + str(self.indicenodo) + "[label=\"" + nodo.getCarnet() + "\\n" + nodo.getNombre() + "\"];\n")
            self.indicenodo += 1
            self.aux_preorden(nodo.getIzquierdo(), "I")
            self.aux_preorden(nodo.getDerecho(), "D")
