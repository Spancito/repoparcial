import math
x0 = 0.8
x = 0.805
h = x - x0
ordenMaximo = 15
estimacionAnterior = 0.0
estimacionActual = 0.0
print(f"{'Orden (n)' :<10} | {'Estimación f(x)':<22} | {'Error relativo (%)':<25}")
print("-" * 65)
for n in range(ordenMaximo+1):
    derivada = ((-1)**n) * math.exp(-x0)
    termino = (derivada/math.factorial(n)) * (h**n)
    estimacionActual += termino
    if n == 0:
        errorStr = "N/A"
    else:
        errorAproximado = abs((estimacionActual - estimacionAnterior) / estimacionActual) * 100
        errorStr = f"{errorAproximado:.10e}%"

    print(f"{n:<10} | {estimacionActual:<22.15f} | {errorStr:<25}")
    estimacionAnterior = estimacionActual
