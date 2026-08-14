#def MostrarTablero(n):
#    print(\t )
#    for i in range (n):
#        print(i)

        


n = int(input("Ingrese la cantidad de casillas: "))

while n < 6 or n > 12:
    print(f" {n} fuera del rango permitido de casillas")
    n = int(input("Ingrese la cantidad de casillas: "))

tablero = [["." for j in range(n)] for i in range(n)]

#for i in range(2):
    #for j in range(n):
       # tablero[i][j] = "B"

#for i in range(n - 2, n):
    #for j in range(n):
        #tablero[i][j] = "N"

#for fila in tablero:
    #print(*fila)


m=0
for i in range(n):
    tablero = [["."for j in range(n)]
               for i in range(n)]
    if m < 2 or m > n-2:
        while m<2:
            for j in range (n):
                tablero[i][j] = "B"
        while m>n-2:            
            for j in range (n):
                tablero[i][j] = "N"   
    m = m + 1


for fila in tablero:
    print(" | ".join(fila))