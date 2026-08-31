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

def miniMax(tablero, leTocaAlAgente):
    global cont
    cont += 1
    
    #CASOS BASE: 
    ganador = buscaGanador(tablero)
    if ganador == 'X':          # PC gana -> 1
        return 1
    elif ganador == 'O':        # HUMANO gana -> -1
        return -1
    elif tableroLleno(tablero): # Empate -> 0
        return 0
    
    #CASOS RECURSIVOS:
    if leTocaAlAgente:
        mejorPuntaje = -inf
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '.':
                    tablero[i][j] = 'X'                 #prueba la jugada i,j
                    puntaje = miniMax(tablero, False)   #Regresa de la recursión
                    tablero[i][j] = '.'                 #borra la jugada i,j
                    mejorPuntaje = max(puntaje, mejorPuntaje)
    else:       #Humano
        mejorPuntaje = inf
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == '.':
                    tablero[i][j] = 'O'     #prueba la jugada i,j
                    puntaje = miniMax(tablero, True)
                    tablero[i][j] = '.'     #borra la jugada i,j
                    mejorPuntaje = min(puntaje, mejorPuntaje)
    return mejorPuntaje

def mejorMovimiento(tablero):
    mejorPuntaje = -inf
    movimiento = None
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == '.':
                tablero[i][j] = 'X'
                puntaje = miniMax(tablero, False)
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
    turno = 'X'  #inicia jugando el agente
    while buscaGanador(tablero) == None and not tableroLleno(tablero):
        imprimeTablero(tablero)
        if turno == 'X':
            (i,j) = mejorMovimiento(tablero)    
            print(f"Número de tableros revisados: {cont}")
            cont = 0
            tablero[i][j] = 'X'
            print("Juego del PC:")
            turno = 'O'
        else:
            fila = int(input("Fila (1,2,3): "))
            columna = int(input("Columna (1,2,3): "))
            if tablero[fila-1][columna-1] == '.':
                tablero[fila-1][columna-1] = 'O'
                turno = 'X'
    ganador = buscaGanador(tablero)
    imprimeTablero(tablero)
    if ganador == 'X':
        print(f"Ganó el PC!")
    elif ganador == 'O':
        print(f"Ganaste!")
    else:
        print("Empate")

####################################
###       BLOQUE PRINCIPAL       ###
####################################

cont = 0
juegoGato()
