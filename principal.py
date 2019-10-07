import curses
import menu

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

menup = menu.menu(window)
menup.pintarmenu()

while True:
    event = window.getch()

    if event == 52:
        break
    else:
        if event == 49:
            menup.pedirarchivo()
            window.clear()
            menup.pintarmenu()
curses.endwin()