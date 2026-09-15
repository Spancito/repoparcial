def Base10ABase12(numero):
    if numero == 0:
        return "0"
    digitos = "0123456789AB"
    resultado = ""
    es_negativo = False
    if numero < 0:
        es_negativo = True
        numero = abs(numero)
    while numero > 0:
        residuo = numero % 12
        resultado = digitos[residuo] + resultado
        numero = numero // 12

    return "-" + resultado if es_negativo else resultado

numeroBase10 = int(input("Digite su número entero a convertir: "))
resultado_b12 = Base10ABase12(numeroBase10)
print(f"El número {numeroBase10} en base 10 equivale a: {resultado_b12} en base 12")
