def primerPunto():
    aList = [4, 8, 12, 15, 18, 20]
    bList = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    cList = []
    dList = []
    for _ in range(25):
        if _ >=1 and _ < 25:
            if _ % 3 == 0:
                cList.append(_)
    for _ in range(21):
        if _ >=5 and _ <= 20:
            if _ % 2 == 0:
                dList.append(_)

    A = set(aList)
    B = set(bList)
    C = set(cList)
    D = set(dList)

    N = set.difference(set.union(set.difference(B, C), A), set.intersection(set.symmetric_difference(A, D), set.union(B, C)))
    print(f"La Primera Operación De Conjuntos Es: {N}")
    M = set.union(set.symmetric_difference(set.difference(A, D), set.union(B, C)), set.intersection(B, (set.intersection(C, D))))
    print(f"La Segunda Operación De Conjuntos Es: {M}")
    G = set.symmetric_difference(set.difference(set.symmetric_difference(C, A), set.intersection(B, D)), set.difference(set.union(B, C), set.union(A, C)))
    print(f"La Tercera Operación De Conjuntos Es: {G}")

def segundoPunto():
    import math
    grupo = 9
    cargos = 3
    cargos2 = 2
    print("A.")
    respuesta_punto_a = (math.factorial(7) / math.factorial(4))
    print("Si se quiere seleccionar 3 cargos diferentes donde no estén María ni Pedro, " \
    f"el grupo será de 7 personas, es decir es: 7!/4! = {respuesta_punto_a}")
    print("-"*32)
    print("B.")
    respuesta_punto_b = (math.factorial(9)/math.factorial(8))
    print("Si se quiere seleccionar 1 cargo de un grupo de 9 personas," \
    f" la operación será 9!/8! = {respuesta_punto_b}")
    print("-"*32)
    print("C.")
    respuesta_punto_c = (math.factorial(8)/math.factorial(6))
    print("Si María será directora, habrán 2 cargos diferentes de un grupo de 8 personas," \
    f" O sea, la operación a realizar será: 8!/6! = {respuesta_punto_c}")

def tercerPunto():
    numerosBase5 = ["34", "203", "445", "2044"]

    for num in numerosBase5:
        try:
            resultado = int(num, 5)
            print(f"El número {num} en base 5 equivale a {resultado} en base 10.")
        except ValueError:
            print(f"Error: '{num}' no es un número válido en base 5.")

def cuartoPunto():
    def Funcion(x):
        return 0.2 * x**3 - 1.5 * x**2 + x - 6.0

    def PrimeraDerivadaExacta(x):
        return 0.6 * x**2 - 3*x + 1

    def SegundaDerivadaExacta(x):
        return 1.6 * x - 3

    valorX = 0.005
    valorVerdaderoPrimera = PrimeraDerivadaExacta(valorX)
    valorVerdaderoSegunda = SegundaDerivadaExacta(valorX)

    print(f"Valor verdadero primera derivada: {valorVerdaderoPrimera}")
    print(f"Valor verdadero segunda derivada: {valorVerdaderoSegunda}")

    for h in [0.005]:
        valorActual = Funcion(valorX)
        valorAdelante = Funcion(valorX + h)
        valorAtras = Funcion(valorX - h)
        valorAdelanteDoble = Funcion(valorX + 2 * h)
        valorAtrasDoble = Funcion(valorX - 2 * h)

        primeraCentral = (valorAdelante - valorAtras) / (2 * h)

        segundaCentral = (valorAdelante - 2 * valorActual + valorAtras) / (h**2)

        print(f"\nResultados para h = {h}:")
        print(f"Primera derivada central: {primeraCentral:.8f}")
        print(f"Segunda derivada central: {segundaCentral:.8f}")

def main():
    print("Primer punto del parcial:")
    primerPunto()
    print("-"*90)
    print("Segundo punto del parcial: ")
    segundoPunto()
    print("-"*90)
    print("Tercer punto del parcial: ")
    tercerPunto()
    print("-"*90)
    print("Cuarto punto del parcial: ")
    cuartoPunto()

if __name__ == "__main__":
    main()
