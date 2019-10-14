import curses
import os
import csv

class menu:
    def __init__(self, window):
        self.window = window
    
    def pintarmenu(self):
        self.window.addstr(15, 41, "1. INSERTAR BLOQUE")
        self.window.addstr(16, 39, "2. SELECCIONAR BLOQUE")
        self.window.addstr(17, 44, "3. REPORTES")
        self.window.addstr(18, 46, "4. SALIR")

    def pedirarchivo(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(16, 41, "NOMBRE DEL ARCHIVO:")        
        self.window.addstr(17, 41, "PRESIONE ENTER PARA CARGAR")
        self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
        path = os.getcwd()
        tecla = -1
        posx = posicioninicial = 61
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if tecla == 27:
                break
            else: 
                if (tecla > 31 and tecla < 127):
                    self.window.clear()
                    self.window.border(0)
                    self.window.addstr(16, 41, "NOMBRE DEL ARCHIVO:")
                    self.window.addstr(17, 41, "PRESIONE ENTER PARA CARGAR")
                    self.window.addstr(0, 0, "PRESIONAR ESC PARA REGRESAR")
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
                                        print(reg)
                                        numero = 0
                                        for carac in reg:
                                            print(carac)
                                            if carac == "CLASS" or carac == "class":
                                                print("Entro a class")
                                                esclass = True
                                                esdata = False
                                            else:
                                                if carac == "DATA" or carac == "data":
                                                    esdata = True
                                                    esclass = False
                                                else:
                                                    if esclass == True:
                                                        clase += carac
                                                        print(clase)
                                                    else:
                                                        if esdata == True:
                                                            data += carac + ","

                                print(clase)
                                data = data[:-1]
                                print(data)
                            else:
                                self.window.addstr(18, 36, "EL ARCHIVO NO EXISTE")