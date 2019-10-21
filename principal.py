import curses
import menu
import listabloques
import socket
import select
import sys
import json
import hashlib

#tamaño de la ventana
ALTO = 35
ANCHO = 100

curses.initscr()
window = curses.newwin(ALTO, ANCHO, 0, 0)
window.timeout(300)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.border(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

menup = menu.menu(window)
menup.pintarmenu()
lista = listabloques.listabloques()
json_Data = {}
datarecibida = None
insertar = False
while True:
    event = window.getch()
#Inicia a escuchar dell servidor
    read_sockets = select.select([server], [], [], 1)[0]
    import msvcrt
    if msvcrt.kbhit(): read_sockets.append(sys.stdin)
    
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
#            print(message.decode('utf-8'))
            if message.decode('utf-8') == 'true':
                #lista.insertar(json_Data["INDEX"], json_Data["TIMESTAMP"], json_Data["CLASS"], json_Data["DATA"], json_Data["PREVIOUSHASH"], json_Data["HASH"])
                #p = prueba()
                insertar = True
                window.addstr(15, 5, "recibido true")
            else: 
                if message.decode('utf-8') == 'false':
                    insertar = False
                    window.addstr(15, 5, "recibido falso")
                    json_Data = {}
                else:
                    #recibe el json del servidor
                    try:
                        json_Data = {}
                        str_json = message.decode('utf-8')
                        print(str_json)
                        #carga el mensaje del servidor al diccionario json_Data
                        json_Data = json.loads(str_json)
                        print(json_Data)
                        if  str(json_Data["INDEX"])=="0":
                            #si la lista esta vacia envia un true al servidor
                            server.sendall('true'.encode('utf-8'))
                            window.addstr(14, 5, "enviado true")
                            sys.stdout.flush()
                        else:
                            #analisisjson.analizar(json_Data["INDEX"], json_Data["TIMESTAMP"], json_Data["CLASS"], json_Data["DATA"], json_Data["PREVIOUSHASH"], json_Data["HASH"], lista)
                            #obtiene los valores del diccionario
                            index = json_Data["INDEX"]
                            timestamp = json_Data["TIMESTAMP"]
                            clase = json_Data["CLASS"]
                            data = json_Data["DATA"]
                            hashprevio = json_Data["PREVIOUSHASH"]
                            hasha = json_Data["HASH"]
                            window.addstr(14, 5, "INSERTADO")
                            #se concatenan los valores para encontrar el hash
                            cadena = str(index)+timestamp+clase+str(data)+str(hashprevio)
                            #auxhash = hashlib.sha256(hashlib.sha256(str(json_Data["INDEX"]).encode('utf-8')+str(json_Data["TIMESTAMP"]).encode('utf-8')+str(json_Data["CLASS"]).encode('utf-8')+str(json_Data["DATA"]).encode('utf-8')+str(json_Data["PREVIOUSHASH"]).encode('utf-8'))).hexdigest()
                            hashnuevo = hashlib.sha256(cadena.encode('utf-8')).hexdigest()
                            if hashnuevo == hasha and hashprevio == lista.getUltimoHash():
                                #si los dos hash coinciden se envia true al servidor
                                server.sendall('true'.encode('utf-8'))
                                window.addstr(14, 5, "enviado true")
                            else:
                                #si no se envia false
                                server.sendall('false'.encode('utf-8'))
                                window.addstr(14, 5, "enviado falso")
                            sys.stdout.flush()
                            print("esjson")
                    except:
                        print("")
#termina de escuchar
#verificacion de insertar
    if insertar and json_Data != None:
        lista.insertar(json_Data["INDEX"], json_Data["TIMESTAMP"], json_Data["CLASS"], json_Data["DATA"], json_Data["PREVIOUSHASH"], json_Data["HASH"])
        insertar = False
        json_Data = None
#termina verificacion de insertar

    if event == 52:
        break
    else:
        if event == 49:
            index, timestamp, clase, data, hashprevio, hashnuevo = menup.pedirarchivo(lista)
            #print(index, timestamp, clase, data, hashprevio, hashnuevo)
#            print(index)
            if index != None and timestamp != None and clase != None and data != None and hashprevio != None and hashnuevo != None:
                print(hashnuevo)
                json1 = {}
                #crear el diccionario del json
                json1 = {
                    'INDEX' : str(index),
                    'TIMESTAMP' : str(timestamp),
                    'CLASS' : str(clase),
                    'DATA' : str(data),
                    'PREVIOUSHASH' : str(hashprevio),
                    'HASH' : str(hashnuevo)
                }
                #vuelve el diccionario un json
                json_str = json.dumps(json1)
                print("enviado")
                print(json_str)
                #envia al servidor el objeto encodeado a utf-8
                server.sendall(json_str.encode('utf-8'))
                sys.stdout.flush()
                #carga el json a un diccionario 
                json_Data = json.loads(json_str)
            window.clear()
            window.border(0)
            menup.pintarmenu()
        else:
            if event == 50:
                datarecibida = lista.seleccionarbloque(window)
                window.clear()
                window.border(0)
                menup.pintarmenu()
            else:
                if event == 51:
                    menup.menureportes(lista, datarecibida)
                    window.clear()
                    window.border(0)
                    menup.pintarmenu()
        
curses.endwin()
server.close()