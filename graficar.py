import pydot
import json
import arbol

class graficar:
    def __init__(self, window):
        self.window = window
        self.arbol = arbol.arbol()

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
            self.recorrerjson(data) 
            print("es json")
        else:
            self.window.addstr(16, 15, "NO HA SELECCIONADO NINGUN BLOQUE")
            while True:
                event = self.window.getch()
                if event == 27:
                    break
        
    def recorrerjson(self, data_json):
        try:
            json_data = json.loads(data_json)
            print(data_json)
            for carac in json_data:
                print(carac)
                if carac == 'value':
                    print(json_data['value'])
                    
                else:
                    if carac == 'left':
                        print("json", json.dumps(json_data['left']))
                        #print(json.loads(str(json_data['left'])))
                        self.recorrerjson(json.dumps(json_data['left']))
                    else:
                        print(json_data['right'])
                        self.recorrerjson(json.dumps(json_data['right']))
        except:
            print("execpt")
    
    def graficar_recorridos(self, data):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
        if data is not None:
            try:
                json_data = json.loads(str(data))
                for dato in json_data:
                    print(dato)
                print("es json")
            except:
                print("no es json")
        else:
            self.window.addstr(16, 15, "NO HA SELECCIONADO NINGUN BLOQUE")
            while True:
                event = self.window.getch()
                if event == 27:
                    break