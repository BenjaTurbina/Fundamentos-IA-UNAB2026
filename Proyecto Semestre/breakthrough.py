#Importacion de la libreria numpy para la creacion de la matriz de juego y otras necesidades
import numpy as np
from math import inf

#Integrantes:
#Maximiliano Urizar
#Franco Gonzalez
#Benjamin Bravo
#NRC: 8334
   
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

# Funcion que verifica la posicion final si es habil para el movimiento, solamente para el humano
def verificar_posicion_final(tablero, mov_ficha_fila, mov_ficha_columna, opcion,texto):
    global ficha_IA 
    cordenada = cordenada_valida(mov_ficha_fila,mov_ficha_columna,tablero)
    # Si la cordena se encuentra fuera de los limites
    if not cordenada:
        print(f"{texto} fuera de los limites!!") 
        return False
    # Obtiene el dato que se encuentra dentro de las cordenas
    casilla = tablero[mov_ficha_fila][mov_ficha_columna]

    # Verificacion de que se tome la ficha correspondiente segun el turno
    if opcion == 1: 
        if ficha_IA == "B": # El humano ocupa fichas negras
            if casilla == "N":
                return True
            else:
                print("Solamente puede mover fichas negras")
                return False
        else: # El humano ocupa fichas blancas
            if casilla == "B":
                return True
            else:
                print("Solamente puede mover fichas blancas")
                return False
            
    # Verifiacion para moviento de casillas
    else:
        if ficha_IA == "B": # Humano fichas negras
            #condicion ocupada por el mismo color
            if casilla == "N":
                print("Casilla ocupada por ficha del mismo color!!")
                return False
            #pieza ocupada por otro color o vacia
            elif (casilla =="*" or casilla =="B") :
                return True
        else: # Humano fichas blancas
            #condicion ocupada por el mismo color
            if casilla == "B":
                print("Casilla ocupada por ficha del mismo color!!")
                return False
            #pieza ocupada por otro color o vacia
            elif (casilla == "*" or casilla== "N"):
                return True

# Funcion para revisar si se cumple una condicion de victoria
def condicion_victoria(tablero):
    restante_b = np.count_nonzero(tablero == "B")
    restante_n = np.count_nonzero(tablero == "N")

    # Condicion de victoria si las fichas de un color son eliminadas por completo
    if restante_b == 0:
        return "N"
    if restante_n == 0:
        return "B"
    # Condicion de victoria si una ficha llego a la fila enemiga
    if "N" in tablero[0]:
        return "N"
    if "B" in tablero[-1]:
        return "B"

    return None

# Funcion de moviento de ficha para el humano
def mover_ficha(tablero,fila,columna,ficha):
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

    moviento_valido = verificar_posicion_final(tablero,nueva_fila,nueva_columna,2,"Movimiento")
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

# Funcion que genera los movientos para la IA
def generar_movimientos(tablero, color):
    # Lista que guarda los movientos
    movimientos = []    
    # Direccion segun la ficha
    if color == "N":
        direccion = -1
    else:
        direccion = 1
    filas, columnas = tablero.shape
    # Ciclo que recorrer todas las casillas
    for i in range(filas):
        for j in range(columnas):
            # Si la ficha en i,j no es de color correspondiete sigue
            if tablero[i][j] != color:
                continue
            # La ficha es valida para el turno, avanza
            nueva_fila = i + direccion
            # Se prueba la ficha en movientos izquierda, recto, derecha
            for nueva_columna in [j - 1, j, j + 1]:
                # Si el moviento analizado no es valido se contia
                if not cordenada_valida(nueva_fila, nueva_columna, tablero):
                    continue
                # Se evalua que se encuentra en la casilla donde se movera la ficha
                destino = tablero[nueva_fila][nueva_columna]
                if nueva_columna == j:
                    # Recto solo si esta vacia
                    if destino == "*":
                        # Agrega las el moviento en forma de lista [[cordenada de origen], [cordenada de destino], .....]
                        movimientos.append(((i,j),(nueva_fila,nueva_columna)))
                else:
                    # diagonal, vacia o comiendo ficha rival
                    if destino != color:
                        movimientos.append(((i,j),(nueva_fila,nueva_columna)))
    # Retorna una lista con las cordenas de origen y cordenas finales de la ficha
    return movimientos

# Funcion que evalua la vulnerabilidad, capturas y distancia de las fichas
def contar_amenazas(tablero, color):
    filas, columnas = tablero.shape
    # Forma de avanze dependiendo de la ficha
    if color == "N":
        direccion = -1     
        enemigo = "B"
    else:
        direccion = 1   
        enemigo = "N"

    # Valores para la evaluacion si se puede capturar una ficha o si corre peligro una ficha
    vulnerabilidad = 0
    capturas_disponibles = 0

    # Ciclo que recorre la matriz 
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] != color:
                continue
            # Evaluacion de si la ficha evaluada corre peligro de ser eliminada por una ficha enemiga
            fila_atacante = i - direccion
            # Se evaluan las direcciones laterales de la posicion
            for columna_atacante in (j - 1, j + 1):
                # Si la cordenada evaluada es valida y las posiciones corresponden a una ficha enemiga se considera vulnerable
                if cordenada_valida(fila_atacante, columna_atacante, tablero) and tablero[fila_atacante][columna_atacante] == enemigo:
                    vulnerabilidad += 1
                    break
            # Evaluacion de si es posible eliminar a una ficha contraria
            fila_destino = i + direccion
            for columna_destino in (j - 1, j + 1):
                # Si hay una ficha contraria para eliminar se considera una posible captura
                if cordenada_valida(fila_destino, columna_destino, tablero) and tablero[fila_destino][columna_destino] == enemigo:
                    capturas_disponibles += 1

    # Distancia de a cuanto se esta de la meta
    distancia_meta = None
    if color == "N":
        for i in range(filas):
            if "N" in tablero[i]:
                distancia_meta = i
                break
    else:
        for i in range(filas - 1, -1, -1):
            if "B" in tablero[i]:
                distancia_meta = filas - 1 - i
                break
    # Retorno con los valores encontrados de las vulnerabilidades, captuas y la distancia a la meta
    return vulnerabilidad, capturas_disponibles, distancia_meta

# Funcion heurisistica que contempla la situacion actual del tablero
def evaluar_tablero(tablero, ficha_IA):
    if ficha_IA == "N":
        ficha_oponente = "B"
    else:
        ficha_oponente = "N"

    filas, columnas = tablero.shape

    # Valores constantes para el calculo de puntajes
    BASE_PIEZA = 10 # Valor por cada pieza de juego
    BONUS_DEFENDIDA = 2 # valor como bus al defender una pieza del mismo color
    PESO_VULNERABILIDAD = 6 # # Valor de una ficha en peligro
    PESO_CAPTURA = 8 # valor de comer una ficha enemiga
    URGENCIA_POR_DISTANCIA = {0: 200, 1: 100, 2: 55, 3: 30, 4: 15} #diccionario donde evalua mayor puntaje a la menor distancia a la meta

    #funcion que retorta el valor de que tan cerca esta la ficha de la meta
    def urgencia(distancia):
        if distancia is None:
            return 0
        return URGENCIA_POR_DISTANCIA.get(distancia, 5)

    #recorre todo el tablero y salta las casillas vacias 
    puntaje = 0
    for i in range(filas):
        for j in range(columnas):
            ficha = tablero[i][j]
            if ficha == "*":
                continue
            # entre mas adelante mayor puntaje, fila_defensa es la fila detras de la ficha 
            # en la posicion i y revisa sus adyaentes para verificar si estan defendido segun su color
            if ficha == "B":
                avance = i
                fila_defensa = i - 1
            else:
                avance = filas - 1 - i
                fila_defensa = i + 1
            # Asignacion del valor que tiene el avance de la ficha y la constante del valor de la ficha
            valor = BASE_PIEZA + avance
            for columna_defensa in (j - 1, j + 1):
                # Si la ficha cuenta con fichas alidas detras en forma diagonal cuenta como posible defendida
                if cordenada_valida(fila_defensa, columna_defensa, tablero) and tablero[fila_defensa][columna_defensa] == ficha:
                    valor += BONUS_DEFENDIDA
                    break
            # Asignacion de puntaje segun favorable para la ia o el humano
            if ficha == ficha_IA:
                puntaje += valor
            else:
                puntaje -= valor

    #llama a la funcion contar amenazas y retorna la vulnerabilidad, capturas y distancia tanto de la IA como el oponente
    vulnerabilidad_ia, capturas_ia, distancia_ia = contar_amenazas(tablero, ficha_IA)
    vulnerabilidad_op, capturas_op, distancia_op = contar_amenazas(tablero, ficha_oponente)

    #amplifica los resultados con los valores y se suma o resta al puntaje en funcion si es a favor o en contra de la IA
    puntaje += PESO_CAPTURA * capturas_ia
    puntaje -= PESO_VULNERABILIDAD * vulnerabilidad_ia
    puntaje -= PESO_CAPTURA * capturas_op
    puntaje += PESO_VULNERABILIDAD * vulnerabilidad_op

    #Se toma en consideracion la urgencia en caso si esta cerca de ganar tanto para la IA como el rival
    puntaje += urgencia(distancia_ia)
    puntaje -= urgencia(distancia_op)    

    #regula los valores para que no se salga del rango aceptable
    puntaje = max(-900, min(900, puntaje))

    return puntaje

# Funcion que evalua el tablero con el moviento de prueba y entrega el mejor moviento
def alfaBetaLimitada(tablero,LeTocaIA,d,alfa,beta):
    global ficha_IA
    global cont
    cont+= 1
    # Seleccion de ficha oponente para la seccion de min
    if ficha_IA== "N":
        ficha_oponente = "B"
    else:
        ficha_oponente = "N"

    # Casos base
    ganador = condicion_victoria(tablero)
    if ganador == ficha_IA:           # Gana la IA
        return 1000
    elif ganador == ficha_oponente:# Gana el humano
        return -1000

    # La poda llega a su limite, se evalua el tablero
    if d == 0:
        return evaluar_tablero(tablero,ficha_IA)

    if LeTocaIA: 
        mejorPuntaje = -inf
        moviento_posible_ia = generar_movimientos(tablero,ficha_IA)
        for moviento_evaluado in moviento_posible_ia:
            # Seleccionamos las cordenadas de prueba
            origen = moviento_evaluado[0] # Cordenada (i_inicio,j_inicio)
            final = moviento_evaluado[1] # Cordenada (i_final,j_final)

            # Se guarda el dato que esta donde se movera ficha, ej: "N" o "*"
            dato_ficha = tablero[final[0]][final[1]]

            # Simulacion del moviento
            # La ficha se mueve de su casilla
            tablero[origen[0]][origen[1]] = "*"
            # La ficha aterriza en su nueva posicion
            tablero[final[0]][final[1]] = ficha_IA
    
            puntaje = alfaBetaLimitada(tablero, False, d-1, alfa, beta)  
                    
            # Se restaura el moviento realizado en el tablero
            tablero[origen[0]][origen[1]] = ficha_IA
            tablero[final[0]][final[1]] = dato_ficha

            mejorPuntaje = max(puntaje, mejorPuntaje)
            alfa = max(alfa, mejorPuntaje)
            if alfa >= beta:
                break
    else:   # La IA evalua el posible moviento del humano
        mejorPuntaje = inf
        moviento_humano_sim = generar_movimientos(tablero,ficha_oponente)
        for moviento_evaluado in moviento_humano_sim:
            origen = moviento_evaluado[0] 
            final = moviento_evaluado[1]
            dato_ficha = tablero[final[0]][final[1]]
            tablero[origen[0]][origen[1]] = "*"
            tablero[final[0]][final[1]] = ficha_oponente
            puntaje = alfaBetaLimitada(tablero, True, d-1, alfa, beta)
            tablero[origen[0]][origen[1]] = ficha_oponente
            tablero[final[0]][final[1]] = dato_ficha
            mejorPuntaje = min(puntaje, mejorPuntaje)
            beta = min(beta, mejorPuntaje)
            if alfa >= beta:
                break
    # Retorna el mejor valor encontrado del tablero simulado
    return mejorPuntaje
    
# Funcion de mejor moviento, realiza una busqueda de cual moviento tiene mayor valor de puntaje
def mejorMovimiento(tablero):
    global ficha_IA
    mejorPuntaje = -inf
    movimiento = None
    # Profundidad del arbol a evaluar
    d = 1
    # generar_moviento realiza los ciclos que leen todo el tablero y 
    # evalua segun la ficha de la IA e retornar un arreglo
    # de forma [[(i_inicio,j_inicio),(i_final,j_final)],[(),()], ...]
    moviento_posible_ia = generar_movimientos(tablero,ficha_IA)
    for moviento_evaluado in moviento_posible_ia:
        # Seleccionamos las cordenadas de prueba
        origen = moviento_evaluado[0] # Cordenada (i_inicio,j_inicio)
        final = moviento_evaluado[1] # Cordenada (i_final,j_final)

        # Se guarda el dato que esta donde se movera ficha, ej: "N" o "*"
        dato_ficha = tablero[final[0]][final[1]]

        # Simulacion del moviento
        # La ficha se mueve de su casilla
        tablero[origen[0]][origen[1]] = "*"
        # La ficha aterriza en su nueva posicion
        tablero[final[0]][final[1]] = ficha_IA

        # Evaluacion del moviento realizado,entregando el tablero con el moviento simulado
        puntaje = alfaBetaLimitada(tablero,False,d,-inf,inf)

        # Se restaura el moviento realizado en el tablero
        tablero[origen[0]][origen[1]] = ficha_IA
        tablero[final[0]][final[1]] = dato_ficha

        # Segun el puntaje obtenido, guarda el mejor moviento de la lista
        if puntaje > mejorPuntaje:
            mejorPuntaje = puntaje
            movimiento = moviento_evaluado
    # Retorna las cordenas mejor encontradas [0] --> conrdenada inicio [1] --> cordenada final
    return movimiento


print("Bienvenido a Brakthrougth\n")

# Creacion de tablero (matriz) NxN 
n = verificar_solo_digito(input("Ingrese un numero de casillas (6 MIN): "))
while n < 6 or n > inf:
    print(f" {n} fuera del rango permitido de casillas")
    n = verificar_solo_digito(input("Ingrese la cantidad de casillas: "))

tablero = crear_tablero(n)

print("--------------- Tablero de juego ---------------")
print(tablero)
print("------------------------------------------------\n")

print("Fichas disponibles\n 1.- Fichas Negras\n 2.- Fichas Blancas\n")

player = verificar_solo_digito(input("Seleccione una ficha: ")) #player sera humano
while player not in [1,2]:
    print("Error!")
    player= verificar_solo_digito(input("Seleccione una ficha: "))

# Seleccion de quien parte
if player == 1:
    # Humano fichas negras, IA fichas blancas
    quien_parte = "Humano"
    ficha_IA = "B"
else:
    # Humano fichas blancas, IA fichas negras
    quien_parte = "IA"
    ficha_IA = "N"

cont = 0
turno_actual = quien_parte
turno = 1
juego_terminado = False

# Se inicializa el juego
while not juego_terminado:
    print(f"\n---------------- Turno N*{turno} ----------------")
    print(tablero)
    
    if turno_actual == 'IA':
        print(f"Juega IA - Fichas {'Blancas' if player == 1 else 'Negras'}:")
        # Se obtienen las cordenadas del mejor moviento econtrado en el tablero
        origen,final = mejorMovimiento(tablero)
        print(f"Número de tableros revisados: {cont}")
        # Se coloca la ficha correspiendiente en el mejor moviento  y se modifica el tablero original
        tablero[origen[0]][origen[1]] = "*"
        tablero[final[0]][final[1]] = ficha_IA
        cont = 0
        print(f"Moviento de la IA realizado desde ({origen[0]},{origen[1]}) hasta ({final[0]},{final[1]})")
        # Cambiamos el turno al humano
        if condicion_victoria(tablero):
            juego_terminado = True
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
            while not verificar_posicion_final(tablero, n_fila, n_columna,1, "Casilla"):
                n_fila = verificar_solo_digito(input("Ingresa la fila: "))
                n_columna = verificar_solo_digito(input("Ingrese la columna: "))

            # Se procede a mover la ficha seleccionada
            resultado = mover_ficha(tablero, n_fila, n_columna, tablero[n_fila][n_columna])

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

ganador = condicion_victoria(tablero)
print("\n¡Juego Finalizado!")
print(f"GANAN LAS FICHAS {'NEGRAS' if ganador == 'N' else 'BLANCAS'}")
print(f"--------- Partida terminada en turno {turno - 1} ----------")
print(tablero)
print("--------------------------------------------------")
