import matplotlib.pyplot as plt
from PIL import Image


def ImagenATensor3D(ruta_imagen):
    img = Image.open(ruta_imagen).convert("RGB")
    ancho, alto = img.size
    pixeles = list(img.getdata())
    tensor = []
    for y in range(alto):
        fila = []
        for x in range(ancho):
            indice = y * ancho + x
            pixel_rgb = pixeles[indice]
            fila.append([pixel_rgb[0], pixel_rgb[1], pixel_rgb[2]])
        tensor.append(fila)

    return tensor


def RGBAGrisTensor2D(tensor_3d):
    vector = (0.299, 0.587, 0.114)

    alto = len(tensor_3d)
    ancho = len(tensor_3d[0])

    tensor2D = []

    for y in range(alto):
        fila_gris = []
        for x in range(ancho):
            r = tensor_3d[y][x][0]
            g = tensor_3d[y][x][1]
            b = tensor_3d[y][x][2]
            intensidad_gris = ((r * vector[0])+(g * vector[1])+(b * vector[2]))
            fila_gris.append(round(intensidad_gris))

        tensor2D.append(fila_gris)

    return tensor2D

ruta = "codes/marioTaller14.png"

tensorRGB = ImagenATensor3D(ruta)
print(f"Tensor 3D creado con éxito. Dimensiones: {len(tensorRGB)}x{len(tensorRGB[0])}x3")

tensorGris = RGBAGrisTensor2D(tensorRGB)
print(f"Tensor 2D de gris creado con éxito. Dimensiones: {len(tensorGris)}x{len(tensorGris[0])}")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(tensorRGB)
plt.title("Imagen Original (Tensor 3D)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(tensorGris, cmap="gray", vmin=0, vmax=255)
plt.title("Escala de Grises (Tensor 2D)")
plt.axis("off")

plt.tight_layout()
plt.show()
