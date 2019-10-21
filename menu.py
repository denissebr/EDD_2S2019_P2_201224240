import curses
import os
import csv
import time
import hashlib
import graficar

class menu:
    def __init__(self, window):
        self.window = window
    
    def pintarmenu(self):
        self.window.addstr(15, 41, "1. INSERTAR BLOQUE")
        self.window.addstr(16, 39, "2. SELECCIONAR BLOQUE")
        self.window.addstr(17, 44, "3. REPORTES")
        self.window.addstr(18, 46, "4. SALIR")

    def menureportes(self, lista, data):
        
        gra = graficar.graficar(self.window)
        while True:
            self.window.clear()
            self.window.border(0)
            self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
            self.window.addstr(0, 46, "REPORTES")
            self.window.addstr(16, 39, "1. REPORTE BLOCKCHAIN")
            self.window.addstr(17, 34, "2. ARBOL DE BLOQUE SELECCIONADO")
            self.window.addstr(18, 38, "3. RECORRIDOS DEL ARBOL")
            event = self.window.getch()
            if event == 49:
                gra.graficar_lista(lista)
            else:
                if event == 27:
                    break
                else:
                    if event == 50:
                        gra.graficar_arbol(data)
                    else:
                        if event == 51:
                            while True:
                                event1 = self.window.getch()
                                self.window.clear()
                                self.window.border(0)
                                self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                                self.window.addstr(0, 41, "TIPOS DE RECORRIDO")
                                self.window.addstr(16, 39, "1. RECORRIDO PREORDEN")
                                self.window.addstr(17, 39, "2. RECORRIDO POSTORDEN")
                                self.window.addstr(18, 40, "3. RECORRIDO INORDEN")
                                if event1 == 27:
                                    break
                                else:
                                    if event1 == 49:
                                        gra.graficar_recorrido_preorden(data)
                                    else:
                                        if event1 == 50:
                                            gra.graficar_recorrido_postorden(data)
                                        else:
                                            if event1 == 51:
                                                gra.graficar_recorrido_inorden(data)

    def pedirarchivo(self, lista):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(16, 41, "NOMBRE DEL ARCHIVO:")        
        self.window.addstr(17, 41, "PRESIONE ENTER PARA CARGAR")
        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
        self.window.addstr(0, 42, "INSERTAR BLOQUE")
        path = os.getcwd()
        tecla = -1
        posx = posicioninicial = 61
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if tecla == 27:
                self.window.addstr(1, 1, "ESC")
                return None, None, None, None, None, None
            else: 
                if (tecla > 31 and tecla < 127):
                    self.window.clear()
                    self.window.border(0)
                    self.window.addstr(16, 41, "NOMBRE DEL ARCHIVO:")
                    self.window.addstr(17, 41, "PRESIONE ENTER PARA CARGAR")
                    self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                    self.window.addstr(0, 42, "INSERTAR BLOQUE")
                    self.window.addstr(16, posicioninicial, auxnombre)
                    self.window.addstr(16, posx, chr(tecla))
                    posx += 1
                    auxnombre += chr(tecla)
                else:
                    if tecla == 8:
                        if posx != posicioninicial:
                            self.window.clear()
                            self.window.border(0)
                            self.window.addstr(16, 41, "NOMBRE DEL ARCHIVO:")
                            self.window.addstr(17, 41, "PRESIONE ENTER PARA CARGAR")
                            self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
                            self.window.addstr(0, 42, "INSERTAR BLOQUE")
                            auxnombre = auxnombre[:-1]
                            self.window.addstr(16, posicioninicial, auxnombre)
                            posx -= 1
                    else:
                        if(tecla == 459 or tecla == 10) and posx != posicioninicial:
                            auxpath = path + "\\bloques\\" + auxnombre
                            if os.path.exists(auxpath):
                                self.window.addstr(18, 36, "EL ARCHIVO EXISTE")
                                esclass = False
                                esdata = False
                                clase = ""
                                data = ""
                                with open(auxpath, newline='') as File:
                                    reader = csv.reader(File)
                                    for reg in reader:
                                        #cada reg es una linea del archivo y cada carac es un campo separado por ,
                                        for carac in reg:
                                            if carac == "CLASS" or carac == "class":
                                                esclass = True
                                                esdata = False
                                            else:
                                                if carac == "DATA" or carac == "data":
                                                    esdata = True
                                                    esclass = False
                                                else:
                                                    if esclass == True:
                                                        clase += carac
                                                    else:
                                                        if esdata == True:
                                                            #como separa todo por , se tiene que concatenar la , para armar el json de la data
                                                            data += carac + ","

                                data = data[:-1]#con esto se le quita el ultimo caracter a la data
                                timestamp = ""
                                timestamp += time.strftime("%d-%m-%y")
                                timestamp += "-::"
                                timestamp += time.strftime("%H:%M:%S")
                                index = lista.getLastIndex()
                                hashprevio = lista.getUltimoHash()
                                auxprevioushash = ""
                                if index == 0:
                                    auxprevioushash = "0000"
                                else:
                                    auxprevioushash = hashprevio
                                #concatena todos los valores para encontrar el hash
                                cadena = str(index)+timestamp+clase+str(data)+auxprevioushash
                                print(cadena)
                                #genera el hash
                                hashnuevo = hashlib.sha256(cadena.encode('utf-8'))
                                #lista.insertar(index, timestamp, clase, data, lista.getUltimoHash(), hashnuevo)
                                return index, timestamp, clase, data, auxprevioushash, hashnuevo.hexdigest()
                            else:
                                self.window.addstr(18, 36, "EL ARCHIVO NO EXISTE")