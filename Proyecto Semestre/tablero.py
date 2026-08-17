# Funcion que verifica que se ingresen solo numeros
def verificar_solo_digito(digito):
    while not isinstance(digito, int):
        try:
            digito = int(digito)
        except ValueError:
            digito = input("Caracter no valido, ingrese nuevamente: ")
    return digito


n = verificar_solo_digito(input("Ingrese un numero de casillas: "))
while n < 6 or n > 12:
    print(f" {n} fuera del rango permitido de casillas")
    n = verificar_solo_digito(input("Ingrese la cantidad de casillas: "))

# Creacion de matriz NxN con caracteres "*" en casa casilla
tablero = [["*" for j in range(n)] for i in range(n)]

# Verificacion de la creacion correcta con el tablero 
for i in tablero:
    print(" | ".join(i))

mitad_tablero = n//2 


print("-----------------------------------------------")    

# Tablero modificado con las fichas negras y blancas en su posicion
for i in range(2):
    for j in range(n):
        tablero[i][j] = "B"
for i in range(n - 2, n):
    for j in range(n):
        tablero[i][j] = "N"

for i in tablero:
    print(" | ".join(i))

