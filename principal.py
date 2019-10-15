import curses
import menu
import listabloques
import socket
import select
import sys
import json

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
while True:
    event = window.getch()

    read_sockets = select.select([server], [], [], 1)[0]
    import msvcrt
    if msvcrt.kbhit(): read_sockets.append(sys.stdin)
    
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message.decode('utf-8'))
            if message.decode('utf-8') == 'true':
                print('true')
            else: 
                if message.decode('utf-8') == 'false':
                    print('false')
                else:
                    str_json = message.decode('utf-8')
                    try:
                        json_Data = json.loads(str_json)
                        print(json_Data["INDEX"])
                    except:
                        print("mensaje")

    if event == 52:
        break
    else:
        if event == 49:
            index, timestamp, clase, data, hashprevio, hashnuevo = menup.pedirarchivo(lista)
            #print(index, timestamp, clase, data, hashprevio, hashnuevo)
            jsona = "{\n\"INDEX\":" + str(index) + ",\n\"TIMESTAMP\":\"" + str(timestamp) + "\",\n\"CLASS\":" + str(clase) + "\",\n\"DATA\":" + str(data) + ",\n\"PREVIOUSHASH\": \"" + str(hashprevio) + "\",\n\"HASH\": \"" + str(hashnuevo) + "\"\n}"
            json1 = {}
            json1 = ({
                'INDEX' : str(index),
                'TIMESTAMP' : str(timestamp),
                'CLASS' : str(clase),
                'DATA' : str(data),
                'PREVIOUSHASH' : str(hashprevio),
                'HASH' : str(hashnuevo)
            })
            json_str = json.dumps(json1, indent=4)
            server.sendall(json_str.encode('utf-8'))
            sys.stdout.flush()
            window.clear()
            window.border(0)
            menup.pintarmenu()
curses.endwin()
server.close()