#Importacion de la libreria numpy para la creacion de la matriz de juego y otras necesidades
import numpy as np
from math import inf

# Funcion que verifica que se ingresen solo numeros
def verificar_solo_digito(digito):
    while not isinstance(digito, int):
        try:
            digito = int(digito)
        except ValueError:
            digito = input("Caracter no valido, ingrese nuevamente: ")
    return digito

# Funcion que crea una matriz NxN
def crear_tablero(casillas):
    tablero = np.full((casillas,casillas),'*')
    for i in range(2):
        for j in range(n):
            tablero[i][j] = "B"
    for i in range(n - 2, n):
        for j in range(n):
            tablero[i][j] = "N"
    return tablero

# Funcion que verifica que la cordenada exista dentro del tablero
def cordenada_valida(fila,columna,tablero):
    limite_fila,limite_columna = tablero.shape
    return (0 <= fila < limite_fila) and (0 <= columna < limite_columna)

# Funcion que verifica la posicion final si es habil para el movimiento
def verificar_posicion_final(tablero, mov_ficha_fila, mov_ficha_columna, turno, opcion,texto): 
    cordenada = cordenada_valida(mov_ficha_fila,mov_ficha_columna,tablero)
    # Si la cordena se encuentra fuera de los limites
    if not cordenada:
        print(f"{texto} fuera de los limites!!") 
        return False
    # Obtiene el dato que se encuentra dentro de las cordenas
    casilla = tablero[mov_ficha_fila][mov_ficha_columna]

    # Verificacion de que se tome la ficha correspondiente segun el turno
    if opcion == 1: 
        if turno % 2 == 1: # negro
            if casilla == "N":
                return True
            else:
                print("Solamente puede mover fichas negras")
                return False
        else: # blanco
            if casilla == "B":
                return True
            else:
                print("Solamente puede mover fichas blancas")
                return False
            
    # Verifiacion para moviento de casillas
    else:
        if turno % 2 == 1: #negro
            #condicion ocupada por el mismo color
            if casilla == "N":
                print("Casilla ocupada por ficha del mismo color!!")
                return False
            #pieza ocupada por otro color o vacia
            elif (casilla =="*" or casilla =="B") :
                return True
        else: #blanco
            #condicion ocupada por el mismo color
            if casilla == "B":
                print("Casilla ocupada por ficha del mismo color!!")
                return False
            #pieza ocupada por otro color o vacia
            elif (casilla == "*" or casilla== "N"):
                return True

# Funcion para revisar si se cumple una condicion de victoria
def condicion_victoria(tablero):
    #  Varibles para la condicion de eliminacion, cuenta cuantas fichas quedan de cada una
    restante_b = np.count_nonzero(tablero == "B")
    restante_n = np.count_nonzero(tablero == "N")

    # Condicion si uno de los colores es eliminado por el otro
    if restante_b == 0:
        print("\nGanan las fichas Negras por eliminacion")
        return  "N"
    if restante_n == 0:
        print("\nGanan las fichas Blancas por eliminacion")
        return "B"
        
    # Condicion si se llega al otro lado contrario
    if "N" in tablero[0]:
        print("\nGanan las fichas Negras por llegar a la meta")
        return "N"
    if "B" in tablero[-1]:
        print("\nGanan las fichas Blancas por llegar a la meta")
        return "B"

    # Retorna falso si nadie a ganado todavia
    return None


# Funcion de moviento de ficha para el humano
def mover_ficha(tablero,fila,columna,ficha,turno):
    if ficha == "N":
        direccion = -1
    else:
        direccion = 1

    print(f"---- FICHA SELECCIONADA: ({fila},{columna}) ----")
    # Opciones de movimiento
    print ("1. Mover izquierda ")
    print ("2. Recto")
    print ("3. Mover derecha")
    print ("4. Seleccionar otra ficha")

    # Verificacion de opcion valida 
    opcion = verificar_solo_digito(input("Ingrese una opcion: "))
    while opcion not in [1,2,3,4 ]:
        print("Opcion no valida")
        opcion = verificar_solo_digito(input("Opcion invalida, ingrese 1, 2, 3, 4 : "))

    # Ficha mueve a la izquierda
    if opcion == 1:
        nueva_fila, nueva_columna =  fila + direccion, columna - 1 
    # Ficha mueve recto
    elif opcion == 2:
        nueva_fila, nueva_columna =  fila + direccion, columna 
    # Ficha mueve a la derecha
    elif opcion == 3:
        nueva_fila, nueva_columna =  fila + direccion, columna + 1
    # Se selecciona otra ficha
    elif opcion == 4:
        return False

    moviento_valido = verificar_posicion_final(tablero,nueva_fila,nueva_columna,turno,2,"Movimiento")
    # Verificacion de si el movimiento es valido
    if not moviento_valido:
        return False

    # Se obtiene el dato que esta en la casilla que se quiere mover 
    destino = tablero[nueva_fila][nueva_columna]

    if opcion == 2:
        if destino != "*":
            print("Movimiento no valido, casilla ocupada")
            return False

    # Se aplica el cambio en el tablero 
    tablero[fila][columna] = "*"
    tablero[nueva_fila][nueva_columna] = ficha

    # Si la condicon de victoria retorna verdadero, se retorna juego terminado
    if condicion_victoria(tablero):
        return "JUEGO TERMINADO"
    
    # Se continua con el siguiente turno
    return "SIGUIENTE TURNO"

#Funcion maxi IA
def generar_movimientos(tablero, color):
    movimientos = []    
    if color == "N":
        direccion = -1
    else:
        direccion = 1
    filas, columnas = tablero.shape
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] != color:
                continue
            nueva_fila = i + direccion
            for nueva_columna in [j - 1, j, j + 1]:
                if not cordenada_valida(nueva_fila, nueva_columna, tablero):
                    continue
                destino = tablero[nueva_fila][nueva_columna]
                if nueva_columna == j:
                    # Recto solo si esta vacia
                    if destino == "*":
                        movimientos.append(((i,j),(nueva_fila,nueva_columna)))
                else:
                    # diagonal, vacia o comiendo ficha rival
                    if destino != color:
                        movimientos.append(((i,j),(nueva_fila,nueva_columna)))
    return movimientos

# Cuenta cuantos movimientos de "color" son capturas (le comen algo al rival)
def contar_amenazas(tablero, color):
    amenazas = 0
    for movimiento in generar_movimientos(tablero, color):
        (fi, ci), (ff, cf) = movimiento
        if tablero[ff][cf] != "*":
            amenazas += 1
    return amenazas

# Heuristica: valor positivo favorece a Blancas, negativo favorece a Negras
def evaluar_tablero(tablero):
    filas, columnas = tablero.shape
    puntaje = 0
    for i in range(filas):
        for j in range(columnas):
            ficha = tablero[i][j]
            if ficha == "*":
                continue
            if ficha == "B":
                avance = i
                fila_defensa = i - 1
            else:
                avance = filas - 1 - i
                fila_defensa = i + 1
            valor = 10 + avance
            defendida = False
            for columna_defensa in [j - 1, j + 1]:
                if cordenada_valida(fila_defensa, columna_defensa, tablero):
                    if tablero[fila_defensa][columna_defensa] == ficha:
                        defendida = True
            if defendida:
                valor += 2
            if ficha == "B":
                puntaje += valor
            else:
                puntaje -= valor

    amenazas_blancas = contar_amenazas(tablero, "B")
    amenazas_negras = contar_amenazas(tablero, "N")
    puntaje += 5 * amenazas_blancas
    puntaje -= 5 * amenazas_negras
    return puntaje


def alfaBetaLimitada(lista_mov,LeTocaIA,d,alfa,beta,tablero,color):
    casillas_x,casillas_y = tablero.shape
    ganador = condicion_victoria(tablero)
    if ganador == "B":
        return 1000
    elif ganador == "N":
        return -1000

    movimientos = generar_movimientos(tablero, color)
        
    if not movimientos:
        if color == "B":
            return -1000
        else:
            return 1000
  
    if d == 0:
        return evaluar_tablero(tablero)

    if LeTocaIA:
        mejorPuntaje = -inf
        for i in range(casillas_x):
            for j in range(casillas_y):
                if tablero[i][j] == "B":
                    
                    puntaje = alfaBetaLimitada(lista_mov,False,d-1,alfa,beta)
                    tablero


    
##IA PROFE
def mejorMovimiento(tablero):
    global player
    casillas_x,casillas_y = tablero.shape #Daria 6,6
    mejorPuntaje = -inf
    movimiento = None
    d = 5 #profundidad del árbol de búsqueda que revisa
    if player == 1 : #IA ES BLANCA
        for i in range(casillas_x):  
            for j in range(casillas_y):   
                if tablero[i][j] == 'B': # Selecciona una
                    moviento_posible_ia = generar_movimientos(tablero,"B")
                    for moviento_eva in moviento_posible_ia:
                        puntaje = alfaBetaLimitada() #puntaje
                        print(f"{(i,j)} ptje: {puntaje}")
                        tablero[i][j] = '*'
                        if puntaje > mejorPuntaje:
                            mejorPuntaje = puntaje
                            movimiento = (i, j)
        return movimiento
    else: #la IA es color negro
        for i in range(casillas_x):  
            for j in range(casillas_y):   
                if tablero[i][j] == 'N': # Selecciona una
                    moviento_posible_ia = generar_movimientos(tablero,"N")
                    for moviento_eva in moviento_posible_ia:
                        puntaje = alfaBetaLimitada()#puntaje
                        print(f"{(i,j)} ptje: {puntaje}")
                        tablero[i][j] = '*'
                        if puntaje > mejorPuntaje:
                            mejorPuntaje = puntaje
                            movimiento = (i, j)
        return movimiento
##

print("Bienvenido a Brakthrougth\n")

# Creacion de tablero (matriz) NxN 
n = verificar_solo_digito(input("Ingrese un numero de casillas (6 MIN/12 MAX): "))
while n < 6 or n > 12:
    print(f" {n} fuera del rango permitido de casillas")
    n = verificar_solo_digito(input("Ingrese la cantidad de casillas: "))

tablero = crear_tablero(n)

print("--------------- Tablero de juego ---------------")
print(tablero)
print("------------------------------------------------\n")

print("Fichas disponibles\n 1.- Fichas negras\n 2.- Fichas Blancas\n")

player = verificar_solo_digito(input("Seleccione una ficha:")) #player sera humano
while player not in [1,2]:
    print("Error!")
    player= verificar_solo_digito(input("Seleccione una ficha: "))


if player == 1:
    quien_parte = "Humano"
else:
    quien_parte = "IA"

turno_actual = quien_parte
turno = 1
juego_terminado = False

# Se inicializa el juego
while not juego_terminado:
    print(f"\n---------------- Turno N*{turno} ----------------")
    print(tablero)
    
    if turno_actual == 'IA':
        print(f"Juega IA - Fichas {'Blancas' if player == 1 else 'Negras'}:")
        # --- AQUÍ IRÁ LA LÓGICA DE LA IA MÁS ADELANTE ---
        # (i,j) = mejorMovimiento(tablero)
        # Aquí la IA moverá su ficha y evaluará si ganó...
        print("La IA está calculando su movimiento... (Lógica pendiente)")
        # Cambiamos el turno al humano
        turno_actual = 'Humano'
        
    else:  # Turno Humano
        print(f"Turno Humano - Fichas {'Negras' if player == 1 else 'Blancas'}")
        bandera_humano = False

        while not bandera_humano:
            print("Seleccione una ficha")
            # Se pide la fila y columna la ficha a mover
            n_fila = verificar_solo_digito(input("Ingresa la fila: "))
            n_columna = verificar_solo_digito(input("Ingrese la columna: "))

            # Se verifica que la posicion sea valida y la ficha correspondiente al turno
            while not verificar_posicion_final(tablero, n_fila, n_columna, turno, 1, "Casilla"):
                n_fila = verificar_solo_digito(input("Ingresa la fila: "))
                n_columna = verificar_solo_digito(input("Ingrese la columna: "))

            # Se procede a mover la ficha seleccionada
            resultado = mover_ficha(tablero, n_fila, n_columna, tablero[n_fila][n_columna], turno)

            # Si resultado retorna juego terminado, se finaliza la partida
            if resultado == "JUEGO TERMINADO":
                bandera_humano = True
                juego_terminado = True
            # Si el moviento es valido, se continua con el siguiente turno
            elif resultado == "SIGUIENTE TURNO":
                bandera_humano = True
            else: 
                print("Error en el movimiento. Seleccione otra ficha.") 
                
        # Cambiamos el turno a la IA
        turno_actual = 'IA'
        
    # Se suma + 1 a los turnos
    turno += 1

print(f"\n--------- Partida terminada en turno {turno - 1} ----------")
print(tablero)
print("¡Juego Finalizado!")
