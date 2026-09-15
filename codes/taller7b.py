def Base6ABase10(cadenaBase6):
    cadenaBase6 = cadenaBase6.strip()

    if not cadenaBase6:
        raise ValueError("Error: No ingresaste ningún número.")

    esNegativo = False
    if cadenaBase6.startswith('-'):
        esNegativo = True
        cadenaBase6 = cadenaBase6[1:]

    digitosPermitidos = set("012345")
    for caracter in cadenaBase6:
        if caracter not in digitosPermitidos:
            raise ValueError(f"Error: El dígito '{caracter}' no es válido para la base 6. Solo se permiten dígitos del 0 al 5.")

    numeroBase10 = 0
    longitud = len(cadenaBase6)

    for i, digito in enumerate(cadenaBase6):
        potencia = longitud - 1 - i
        valorDigito = int(digito)
        numeroBase10 += valorDigito * (6 ** potencia)

    return -numeroBase10 if esNegativo else numeroBase10

try:
    entrada_usuario = input("Ingresa un número entero en base 6: ")
    resultado = Base6ABase10(entrada_usuario)
    print(f"El número {entrada_usuario.strip()} en base 6 equivale a: {resultado} en base 10")
except ValueError as error:
    print(error)
