import struct

def EnteroABits(numero):
    numBits = struct.pack('>h', numero)
    entero16 = struct.unpack('>H', numBits)[0]
    return [int(b) for b in f"{entero16:016b}"]

def BitsAEntero(bits):
    cadenaBits = "".join(map(str, bits))
    entero16 = int(cadenaBits, 2)
    empaquetado = struct.pack('>H', entero16)
    return struct.unpack('>h', empaquetado)[0]

def SumaBinarios16Bits(bits1, bits2):
    num1 = BitsAEntero(bits1)
    num2 = BitsAEntero(bits2)
    suma16 = (num1 + num2) & 0xFFFF
    return [int(b) for b in f"{suma16:016b}"]

def main():
    numero1 = int(input("Ingrese el primer número entero (-32768 a 32767): "))
    numero2 = int(input("Ingrese el segundo número entero (-32768 a 32767): "))

    rango = range(-32768, 32768)
    if numero1 not in rango or numero2 not in rango:
        print("Error: Los números deben estar entre -32768 hasta 32767")
        return

    bits1 = EnteroABits(numero1)
    bits2 = EnteroABits(numero2)
    bitsSuma = SumaBinarios16Bits(bits1, bits2)
    resultadoDecimal = BitsAEntero(bitsSuma)

    print(f"\nNúmero 1: {bits1}")
    print(f"Número 2: {bits2}")
    print(f"Suma Binaria: {bitsSuma}")
    print(f"Resultado Base 10: {resultadoDecimal}")

if __name__ == "__main__":
    main()
