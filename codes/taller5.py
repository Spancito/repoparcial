import math
error_aproximado = 100
cifras_significativas = 8
es = 0.5 * 10**(2-cifras_significativas)
val = 0.0
iteraciones = 0
potencia = 0
signo = 1
x = float(input("Escoja el valor (en radianes): "))
while error_aproximado >= es:
    ant = val
    val += signo * (x**potencia / math.factorial(potencia))
    iteraciones += 1
    if iteraciones > 1:
        error_aproximado = abs((val-ant)/val)*100
    signo *= -1
    potencia+=2

print(f"valor de Cos({x}): {val}")
print(f"error aproximado: {error_aproximado:.8f}%")
print(f"iteraciones: {iteraciones}")
