from math import inf

def imprimeTablero(tablero):
    print()
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()
    print()

def tableroLleno(tablero):
    for fila in tablero:
        if '.' in fila:
            return False
    return True

def buscaGanador(tablero):
    # revisa FILAS
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != '.':
            return fila[0]
    # revisa COLUMNAS
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != '.':
            return tablero[0][col]
    # revisa DIAGONAL PPAL.
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != '.':
        return tablero[0][0]
    # revisa DIAGONAL SECUND.
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != '.':
        return tablero[0][2]
    return None

def estimacion(tablero):
    aX = 0
    aO = 0
    pX = 0
    pO = 0
    c = 0
    if tablero[1][1] == "X":
        c = 1
    elif tablero[1][1] == "O":
        c = -1

    for fila in tablero:
        contX = fila.count("X")
        contO = fila.count("O")
        contE = fila.count(".")
        if contX == 2 and contE == 1:
            aX += 1
        if contO == 2 and contE == 1:
            aO += 1
        if contX == 1 and contE == 2:
            pX += 1
        if contO == 1 and contE == 2:
            pO += 1

    for j in range(3):
        col = []
        for i in range(3):
            col.append(tablero[i][j])
        contX = col.count("X")
        contO = col.count("O")
        contE = col.count(".")
        if contX == 2 and contE == 1:
            aX += 1
        if contO == 2 and contE == 1:
            aO += 1
        if contX == 1 and contE == 2:
            pX += 1
        if contO == 1 and contE == 2:
            pO += 1

    diag = [tablero[0][0], tablero[1][1], tablero[2][2]]
    contX = diag.count("X")
    contO = diag.count("O")
    contE = diag.count(".")
    if contX == 2 and contE == 1:
        aX += 1
    if contO == 2 and contE == 1:
        aO += 1
    if contX == 1 and contE == 2:
        pX += 1
    if contO == 1 and contE == 2:
        pO += 1            

    diag = [tablero[0][2], tablero[1][1], tablero[2][0]]
    contX = diag.count("X")
    contO = diag.count("O")
    contE = diag.count(".")
    if contX == 2 and contE == 1:
        aX += 1
    if contO == 2 and contE == 1:
        aO += 1
    if contX == 1 and contE == 2:
        pX += 1
    if contO == 1 and contE == 2:
        pO += 1

    return 0.1*(aX-aO) + 0.02*(pX-pO) + 0.01*c


def alfaBetaLimitada(tablero, leTocaAlAgente, d, alfa, beta):
    global cont
    cont += 1
    #CASOS BASE: 
    ganador = buscaGanador(tablero)
    if ganador == 'X':          # agente gana -> 1
        return 1
    elif ganador == 'O':        # humano gana -> -1
        return -1
    elif tableroLleno(tablero): # empate -> 0
        return 0

    if d == 0:
        return estimacion(tablero)

    #CASOS RECURSIVOS: 
    if leTocaAlAgente:       
        mejorPuntaje = -inf
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '.':
                    tablero[i][j] = 'X'                             #prueba la jugada i,j
                    puntaje = alfaBetaLimitada(tablero, False, d-1, alfa, beta)   #Regresa de la recursión
                    tablero[i][j] = '.'                             #borra la jugada i,j
                    mejorPuntaje = max(puntaje, mejorPuntaje)
                    alfa = max(alfa, mejorPuntaje)
                    if alfa >= beta:
                        break
    else:       #Humano
        mejorPuntaje = inf
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '.':
                    tablero[i][j] = 'O'
                    puntaje = alfaBetaLimitada(tablero, True, d-1, alfa, beta) #Regresa de la recursión
                    tablero[i][j] = '.'
                    mejorPuntaje = min(puntaje, mejorPuntaje) 
                    beta = min(beta, mejorPuntaje)
                    if alfa >= beta:
                        break
    return mejorPuntaje

def mejorMovimiento(tablero):
    mejorPuntaje = -inf
    movimiento = None
    d = 1 #profundidad del árbol de búsqueda que revisa
    for i in range(3):  
        for j in range(3):   
            if tablero[i][j] == '.':
                tablero[i][j] = 'X'
                puntaje = alfaBetaLimitada(tablero, False, d, -inf, inf)
                print(f"{(i,j)} ptje: {puntaje}")
                tablero[i][j] = '.'
                if puntaje > mejorPuntaje:
                    mejorPuntaje = puntaje
                    movimiento = (i, j)
    return movimiento


#INTERFAZ del juego
def juegoGato():
    global cont
    tablero = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
    turno = 'X' #inicia el agente
    while buscaGanador(tablero) == None and not tableroLleno(tablero):
        imprimeTablero(tablero)
        if turno == 'X':
            (i,j) = mejorMovimiento(tablero)   
            print(f"Número de tableros revisados: {cont}")
            cont = 0
            tablero[i][j] = 'X'
            print("Juego del PC:")
            turno = 'O'
        else:  # humano
            fila = int(input("Fila (1,2,3): "))
            columna = int(input("Columna (1,2,3): "))
            if tablero[fila-1][columna-1] == '.':
                tablero[fila-1][columna-1] = 'O'
                turno = 'X'
    ganador = buscaGanador(tablero)
    imprimeTablero(tablero)
    if ganador:
        print(f"El ganador es: {ganador}")
    else:
        print("Empate")

####################################
###       BLOQUE PRINCIPAL       ###
####################################

cont = 0
juegoGato()
