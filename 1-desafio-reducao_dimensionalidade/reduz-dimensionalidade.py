import numpy as np
from matplotlib import pyplot as plt
import imageio.v3 as iio

# Carregar imagem
imagem_colorida = iio.imread("lena.jpg")

# Criar uma matriz para armazenar a imagem em tons de cinza
altura, largura, _ = imagem_colorida.shape
imagem_cinza = np.zeros((altura, largura), dtype=np.uint8)

# Percorrer cada pixel e converter para escala de cinza
for i in range(altura):
    for j in range(largura):
        r, g, b = imagem_colorida[i, j]
        # Aplicar a fórmula de conversão
        cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
        imagem_cinza[i, j] = cinza


# Definir um limiar para a conversão
limiar = 100

# Criar uma nova matriz para armazenar a imagem em preto e branco
imagem_pb = np.zeros((altura, largura), dtype=np.uint8)

# Aplicar o limiar para cada pixel
for i in range(altura):
    for j in range(largura):
        imagem_pb[i, j] = 255 if imagem_cinza[i, j] > limiar else 0



# Imagem original
plt.subplot(1, 3, 1)
plt.imshow(imagem_colorida)
plt.title("Imagem Colorida")
plt.axis("off")

# Imagem em escala de cinza
plt.subplot(1, 3, 2)
plt.imshow(imagem_cinza, cmap="gray")
plt.title("Escala de Cinza")
plt.axis("off")

# Imagem preto e branco
plt.subplot(1, 3, 3)
plt.imshow(imagem_pb, cmap="gray")
plt.title("Preto e Branco")
plt.axis("off")

# Mostrar as imagens
plt.tight_layout()
plt.show()