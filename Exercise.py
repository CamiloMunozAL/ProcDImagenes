import numpy as np
import matplotlib.pyplot as plt

#Diccionario de colores en formato RGB
colors = {
    "white":     [255, 255, 255],
    "red":       [255, 0, 0],
    "yellow":    [255, 255, 0],
    "green":     [0, 255, 0],
    "cyan":      [0, 255, 255],

    "gray":      [128, 128, 128],
    "dark_red":  [128, 0, 0],
    "blue":      [0, 0, 255],
    "mint":      [128, 255, 212],
    "black":     [0, 0, 0]
}

#Imagen es un arreglo de 2 dimensiones (2 filas y 5 columnas) y 3 canales de color (RGB)
#se especifica el tipo de dato como uint8 (enteros sin signo de 8 bits) para representar los valores de color
image= np.zeros((2,5,3), dtype=np.uint8)

#Se asignan los colores a cada pixel de la imagen utilizando el diccionario de colores
image[0,0] = colors["white"]
image[0,1] = colors["red"]
image[0,2] = colors["yellow"]
image[0,3] = colors["green"]
image[0,4] = colors["blue"]
image[1,0] = colors["cyan"]
image[1,1] = colors["gray"]
image[1,2] = colors["dark_red"]
image[1,3] = colors["mint"]
image[1,4] = colors["black"]

Graphic = plt.imshow(image)  # Muestra la imagen utilizando Matplotlib
plt.title("Imagen de 2x5 con colores")  # Agrega un título a la imagen
plt.xticks(np.arange(-0.5, 5, 1))  # Configura las marcas del eje x
plt.yticks([-0.5, 0.5])
plt.grid(color='black', linestyle='-', linewidth=2)  # Agrega una cuadrícula a la imagen  
plt.show()  # Muestra la imagen