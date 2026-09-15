def Funcion(x):
    return 0.12 * x**3 - 0.5 * x**2 + 2.5

def PrimeraDerivadaExacta(x):
    return 0.36 * x**2 - x

def SegundaDerivadaExacta(x):
    return 0.72 * x - 1.0

valorX = 0.5
valorVerdaderoPrimera = PrimeraDerivadaExacta(valorX)
valorVerdaderoSegunda = SegundaDerivadaExacta(valorX)

print(f"Valor verdadero primera derivada: {valorVerdaderoPrimera}")
print(f"Valor verdadero segunda derivada: {valorVerdaderoSegunda}")

for h in [0.1, 0.05]:
    valorActual = Funcion(valorX)
    valorAdelante = Funcion(valorX + h)
    valorAtras = Funcion(valorX - h)
    valorAdelanteDoble = Funcion(valorX + 2 * h)
    valorAtrasDoble = Funcion(valorX - 2 * h)
    
    primeraAdelante = (valorAdelante - valorActual) / h
    primeraAtras = (valorActual - valorAtras) / h
    primeraCentral = (valorAdelante - valorAtras) / (2 * h)
    
    segundaAdelante = (valorAdelanteDoble - 2 * valorAdelante + valorActual) / (h**2)
    segundaAtras = (valorActual - 2 * valorAtras + valorAtrasDoble) / (h**2)
    segundaCentral = (valorAdelante - 2 * valorActual + valorAtras) / (h**2)
    
    print(f"\nResultados para h = {h}:")
    print(f"Primera derivada hacia adelante: {primeraAdelante:.6f}")
    print(f"Primera derivada hacia atrás: {primeraAtras:.6f}")
    print(f"Primera derivada central: {primeraCentral:.6f}")
    print(f"Segunda derivada hacia adelante: {segundaAdelante:.6f}")
    print(f"Segunda derivada hacia atrás: {segundaAtras:.6f}")
    print(f"Segunda derivada central: {segundaCentral:.6f}")

print("\nComparación para h = 0.05 vs h = 0.1:")
print("Sí, los resultados con h = 0.05 son mejores porque el error de truncamiento en las fórmulas disminuye al reducir el tamaño de paso")