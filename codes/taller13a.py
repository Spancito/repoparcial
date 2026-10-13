import random

primerVector = []
segundoVector = []
print("Digite la longitud del vector: ")
longitudVectores = int(input(">>> "))

for i in range(longitudVectores):
    primerVector.append(random.randint(-10, 10))
    segundoVector.append(random.randint(-10, 10))

print("Los vectores generados fueron:")
print(f"primer vector: {primerVector}")
print(f"segundo vector: {segundoVector}")
print("Digite el valor del escalar por el cual quiera multiplicar cada vector: ")
escalar = int(input(">>> "))
for _ in range(len(primerVector)):
    primerVector[_] = escalar*primerVector[_]
    segundoVector[_] = escalar*segundoVector[_]

print("Vectores resultantes: ")
print(f"primer vector: {primerVector}")
print(f"segundo vector: {segundoVector}")
