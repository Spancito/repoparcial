import random

def CrearMatriz(filas, columnas):
    return [[random.randint(-10, 10) for _ in range(columnas)] for _ in range(filas)]

def ImprimirMatriz(matriz):
    for fila in matriz:
        print([f"{elemento:4}" for elemento in fila])

def main():
    print("Seleccione una operación matricial:\n1. Suma\n2. Multiplicación")
    
    opcion = int(input("Ingrese 1 o 2: "))

    if opcion == 1:
        filas = random.randint(2, 8)
        columnas = random.randint(2, 8)
        primerMatriz = CrearMatriz(filas, columnas)
        segundaMatriz = CrearMatriz(filas, columnas)
        
        resultado = [[primerMatriz[i][j] + segundaMatriz[i][j] for j in range(columnas)] for i in range(filas)]
        
        print(f"Matriz A ({filas}x{columnas}):")
        ImprimirMatriz(primerMatriz)
        print(f"Matriz B ({filas}x{columnas}):")
        ImprimirMatriz(segundaMatriz)
        print("Resultado:")
        ImprimirMatriz(resultado)

    elif opcion == 2:
        filasPrimerMatriz = random.randint(2, 8)
        columnasPrimerMatriz = random.randint(2, 8)
        filasSegundaMatriz = columnasPrimerMatriz
        columnasSegundaMatriz = random.randint(2, 8)
        
        primerMatriz = CrearMatriz(filasPrimerMatriz, columnasPrimerMatriz)
        segundaMatriz = CrearMatriz(filasSegundaMatriz, columnasSegundaMatriz)
        
        resultado = [[sum(primerMatriz[i][k] * segundaMatriz[k][j] for k in range(columnasPrimerMatriz)) for j in range(columnasSegundaMatriz)] for i in range(filasPrimerMatriz)]
        
        print(f"Matriz A ({filasPrimerMatriz}x{columnasPrimerMatriz}):")
        ImprimirMatriz(primerMatriz)
        print(f"Matriz B ({filasSegundaMatriz}x{columnasSegundaMatriz}):")
        ImprimirMatriz(segundaMatriz)
        print(f"Resultado de la Multiplicación ({filasPrimerMatriz}x{columnasSegundaMatriz}):")
        ImprimirMatriz(resultado)

if __name__ == "__main__":
    main()