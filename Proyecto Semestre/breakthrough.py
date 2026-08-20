#Importacion de la libreria numpy para la creacion de la matriz de juego
import numpy as np

# COSAS QUE VERIFICAR
    # Condicion de victoria
    # Moviento de fichas fuera de la matriz, da error


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
def verificar_posicion_final(tablero, mov_ficha_fila, mov_ficha_columna, turno, opcion): 
    cordenada = cordenada_valida(mov_ficha_fila,mov_ficha_columna,tablero)
    # Si la cordena se encuentra fuera de los limites
    if not cordenada:
        print("Cordenada fuera de los limites!!") 
        return False
    # Obtiene el dato que se encuentra dentro de las cordenas
    casilla = tablero[mov_ficha_fila][mov_ficha_columna]
    # Verificacion para seleccion de ficha
    if opcion == 1: 
        if turno % 2 == 1: # negro
            if casilla == "N":
                return True
            else:
                print(f"Ficha seleccionada no valida para el turno {turno} !negro!")
                return False
        else: # blanco
            if casilla == "B":
                return True
            else:
                print(f"Ficha seleccionada no valida para el turno {turno} !blanco!")
                return False
    # Verifiacion para moviento de casillas 
    else:
        if turno % 2 == 1: #negro
            #condicion  ocupada por el mismo color
            if casilla == "N":
                return False
            #pieza ocupada por otro color o vacia
            elif (casilla =="*" or casilla =="B") :
                return True
        else: #blanco
            #condicion ocupada por el mismo color
            if casilla == "B":
                return False
            #pieza ocupada por otro color o vacia
            elif (casilla == "*" or casilla== "N"):
                return True


# funcion de movimiento fichas
def mover_ficha(tablero,fila,columna,ficha,turno):
    # return que indique si los 3 movientos son validos, sino que seleccione otra ficha
    n =len((tablero))
    if ficha == "N":
        direccion = -1
    else:
        direccion = 1
    print ("1. mover izquierda ")
    print ("2. recto")
    print ("3. mover derecha")

    opcion = verificar_solo_digito(input("Ingrese una opcion: "))
    while opcion not in [1,2,3] and (verificar_posicion_final(tablero,fila -1,columna + direccion,turno,2) or verificar_posicion_final(tablero,fila,columna + direccion,turno,2) or verificar_posicion_final(tablero,fila +1,columna + direccion,turno,2)):
        print("Opcion no valida")
        opcion = verificar_solo_digito(input("Opcion invalida, ingrese 1, 2, 3: "))
    if opcion == 1:
        nueva_fila, nueva_columna =  fila + direccion, columna - 1 
    elif opcion == 2:
        nueva_fila, nueva_columna =  fila + direccion, columna 
    elif opcion == 3:
        nueva_fila, nueva_columna =  fila + direccion, columna + 1
    else:
        print("Fallo")
    if nueva_fila < 0 or nueva_fila >= n or nueva_columna < 0 or nueva_columna >= n:
        print("Movimiento no valido, fuera de los limites del tablero")

    destino = tablero[nueva_fila][nueva_columna]

    if opcion == 2:
        if destino != "*":
            print("Movimiento no valido, casilla ocupada")
            return False
    else:
        if destino == ficha:
            print("no se puede capturar una ficha propia, movimiento no valido")
            return False
    tablero[fila][columna] = "*"
    tablero[nueva_fila][nueva_columna] = ficha
    return True
    



    
    

# Creacion de tablero (matriz) NxN 

n = verificar_solo_digito(input("Ingrese un numero de casillas: "))
while n < 6 or n > 12:
    print(f" {n} fuera del rango permitido de casillas")
    n = verificar_solo_digito(input("Ingrese la cantidad de casillas: "))


tablero = crear_tablero(n)

turno = 0
# Simplificar codigo con funcion para el moviento tanto de fichas blancas o negras
while True:
    bandera_negra = False
    bandera_blanca = False
    turno += 1
    if turno % 2 == 1:
        while not bandera_negra:
            print(f"---------------- Turno N*{turno}: Fichas Negras ----------------")
            print(tablero)
            print("Seleccione una ficha")
            # Se pide la fila y columna la ficha a mover
            n_fila = verificar_solo_digito(input("Ingresa la fila: "))
            n_columna = verificar_solo_digito(input("Ingrese la columna: "))
            # Se verifica que la posicion sea valida y la ficha correspondiente al turno
            while not verificar_posicion_final(tablero,n_fila,n_columna,turno,1):
                n_fila = verificar_solo_digito(input("Ingresa la fila: "))
                n_columna = verificar_solo_digito(input("Ingrese la columna: "))
            # Se procede a mover la ficha selecciona
            if mover_ficha(tablero,n_fila,n_columna,tablero[n_fila][n_columna],turno):
                bandera_negra = True
            else:
                print("Hay un error en el moviento")
            #actualizar tablero

    else:
        print(f"---------------- Turno N*{turno}: Fichas Blancas ----------------")
        while not bandera_blanca:   
            print(tablero)
            print("Seleccione una ficha")           
            n_fila = verificar_solo_digito(input("Ingresa la fila: "))
            n_columna = verificar_solo_digito(input("Ingrese la columna: "))
            while not verificar_posicion_final(tablero,n_fila,n_columna,turno,1):
                n_fila = verificar_solo_digito(input("Ingresa la fila: "))
                n_columna = verificar_solo_digito(input("Ingrese la columna: "))
            # Se procede a mover la ficha selecciona
            if mover_ficha(tablero,n_fila,n_columna,tablero[n_fila][n_columna],turno):
                bandera_blanca = True
            else:
                print("Hay un error en el moviento")
            #actualizar tablero