#Importacion de la libreria numpy para la creacion de la matriz de juego
import numpy as np

# Funcion que verifica que se ingresen solo numeros
def verificar_solo_digito(digito):
    while not isinstance(digito, int):
        try:
            digito = int(digito)
        except ValueError:
            digito = input("Caracter no valido, ingrese nuevamente: ")
    return digito

# Funcion que verifica la posicion esta en el tablero
def verificar_posicion(n):


# Main del codigo
n = verificar_solo_digito(input("Ingrese un numero de casillas: "))
while n < 6 or n > 12:
    print(f" {n} fuera del rango permitido de casillas")
    n = verificar_solo_digito(input("Ingrese la cantidad de casillas: "))

# Creacion de matriz NxN con caracteres "*" en casa casilla
tablero = np.full((n,n),'*')



# Tablero modificado con las fichas negras y blancas en su posicion
for i in range(2):
    for j in range(n):
        tablero[i][j] = "B"
for i in range(n - 2, n):
    for j in range(n):
        tablero[i][j] = "N"


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

            # Crear una condicion donde se coloquen cordenadas validas dentro de la matriz    
                   
            mov_ficha_fila = verificar_solo_digito(input("Ingrese fila: "))
            mov_ficha_columa =  verificar_solo_digito(input("Ingrese columna: "))
            print(f"Cordenadas ficha seleccionada: {mov_ficha_fila},{mov_ficha_columa}")
            valor_encontrado = tablero[mov_ficha_fila][mov_ficha_columa]
            if valor_encontrado == "N":
                print(f"Ficha Negra: {mov_ficha_fila},{mov_ficha_columa} seleccionada")
                bandera_negra = True
            # Colocar una opcion si la ficha no tiene capacidad de moviento (En turno 1 solamente se podrian mover las fichas de delante)

            # Si el valor no corresponde algo dentro de la matriz muestra
            else:
                print("Ficha seleccionada no valida para el turno!")
        print("Has salido del ciclo while al seleccionar la correcta!!")
    else:
        print(f"---------------- Turno N*{turno}: Fichas Blancas ----------------")
        while not bandera_blanca:   
            print(tablero)
            print("Seleccione una ficha")           
            mov_ficha_fila = verificar_solo_digito(input("Ingrese fila: "))
            mov_ficha_columa =  verificar_solo_digito(input("Ingrese columna: "))
            # Crear una condicion donde se coloquen cordenadas validas dentro de la matriz
            print(f"Cordenadas ficha seleccionada: {mov_ficha_fila},{mov_ficha_columa}")
            valor_encontrado = tablero[mov_ficha_fila][mov_ficha_columa]
            if valor_encontrado == "B":
                print(f"Ficha Blanca: {mov_ficha_fila},{mov_ficha_columa} seleccionada")
                bandera_blanca = True
            # Colocar una opcion si la ficha no tiene capacidad de moviento (En turno 1 solamente se podrian mover las fichas de delante)

            # Si el valor no corresponde algo dentro de la matriz muestra
            else:
                print("Ficha seleccionada no valida para el turno!")
        print("Has salido del ciclo while al seleccionar la correcta!!")