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
            else: 
                if message.decode('utf-8') == 'false':
                    insertar = False
                    json_Data = {}
                else:
                    try:
                        json_Data = {}
                        str_json = message.decode('utf-8')
                        print(str_json)
                        json_Data = json.loads(str_json)
                        print(json_Data)
                        if lista.estavacia() == True:
                            server.sendall('true'.encode('utf-8'))
                            sys.stdout.flush()
                        else:
                            #analisisjson.analizar(json_Data["INDEX"], json_Data["TIMESTAMP"], json_Data["CLASS"], json_Data["DATA"], json_Data["PREVIOUSHASH"], json_Data["HASH"], lista)
                            index = json_Data["INDEX"]
                            timestamp = json_Data["TIMESTAMP"]
                            clase = json_Data["CLASS"]
                            data = json_Data["DATA"]
                            hashprevio = json_Data["PREVIOUSHASH"]
                            hasha = json_Data["HASH"]
                            #auxhash = hashlib.sha256(hashlib.sha256(str(json_Data["INDEX"]).encode('utf-8')+str(json_Data["TIMESTAMP"]).encode('utf-8')+str(json_Data["CLASS"]).encode('utf-8')+str(json_Data["DATA"]).encode('utf-8')+str(json_Data["PREVIOUSHASH"]).encode('utf-8'))).hexdigest()
                            hashnuevo = hashlib.sha256(str(index).encode('utf-8')+str(timestamp).encode('utf-8')+str(clase).encode('utf-8')+str(data).encode('utf-8')+str(hashprevio).encode('utf-8')).hexdigest()
                            if hashnuevo == hasha and hashprevio == lista.getUltimoHash():
                                server.sendall('true'.encode('utf-8'))
                            else:
                                server.sendall('false'.encode('utf-8'))
                            sys.stdout.flush()
                            print("esjson")
                    except:
                        print("")

    if insertar and json_Data != None:
        lista.insertar(json_Data["INDEX"], json_Data["TIMESTAMP"], json_Data["CLASS"], json_Data["DATA"], json_Data["PREVIOUSHASH"], json_Data["HASH"])
        insertar = False
        json_Data = None

    if event == 52:
        break
    else:
        if event == 49:
            index, timestamp, clase, data, hashprevio, hashnuevo = menup.pedirarchivo(lista)
            #print(index, timestamp, clase, data, hashprevio, hashnuevo)
#            print(index)
            if index != None and timestamp != None and clase != None and data != None and hashprevio != None and hashnuevo != None:
                jsona = "{\n\"INDEX\":" + str(index) + ",\n\"TIMESTAMP\":\"" + str(timestamp) + "\",\n\"CLASS\":" + str(clase) + "\",\n\"DATA\":" + str(data) + ",\n\"PREVIOUSHASH\": \"" + str(hashprevio) + "\",\n\"HASH\": \"" + str(hashnuevo) + "\"\n}"
                json1 = {}
                json1 = {
                    'INDEX' : str(index),
                    'TIMESTAMP' : str(timestamp),
                    'CLASS' : str(clase),
                    'DATA' : str(data),
                    'PREVIOUSHASH' : str(hashprevio),
                    'HASH' : str(hashnuevo)
                }
                json_str = json.dumps(json1)
                print(json1)
                server.sendall(json_str.encode('utf-8'))
                sys.stdout.flush()
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