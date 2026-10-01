# Taller 3 – Ecualización y transformaciones de intensidad

Este repositorio contiene el desarrollo del **Taller 3 de Procesamiento Digital de Imágenes**, enfocado en modificar la distribución de intensidades de imágenes en escala de grises y de imágenes a color.

## Contenido

El taller desarrolla los siguientes puntos:

1. Ecualización global de una imagen en escala de grises con `cv2.equalizeHist`.
2. Comparación de los histogramas original y ecualizado.
3. Oscurecimiento de la imagen mediante la transformación `y = x / 3`.
4. Aclaramiento de la imagen mediante la transformación `y = 1.3x`, limitada al rango `[0, 255]`.
5. Reducción del contraste mediante `y = 0.5x + 64`.
6. Aumento del contraste mediante `y = 2x − 128`, con saturación al rango válido.
7. Aplicación de una transformación gamma a cada canal de una imagen a color.

## Concepto principal

Las transformaciones de intensidad modifican el valor de cada píxel manteniendo, en general, su posición. Estas operaciones pueden cambiar el brillo, el contraste o la distribución global de los niveles de gris.

La ecualización global busca redistribuir las intensidades para aprovechar mejor el rango de 0 a 255. En cambio, las transformaciones lineales utilizadas en los puntos 3 a 6 aplican una fórmula explícita a cada píxel. Después de cada operación se calcula el histograma para observar cómo cambió la distribución.

## Resultados y análisis

La imagen original tiene intensidades entre 0 y 255 y un promedio aproximado de `126.18`. Después de usar `cv2.equalizeHist`, el rango continúa siendo 0–255, pero el promedio aumenta ligeramente hasta aproximadamente `127.33`, indicando una redistribución más equilibrada de las intensidades.

Al oscurecer la imagen con `x / 3`, el máximo pasa a 85 y el promedio disminuye hasta aproximadamente `41.73`. Esto concentra el histograma en la zona de intensidades bajas.

Al aclarar la imagen con `1.3x`, algunos valores superan 255 y deben recortarse mediante `np.clip`. El promedio aumenta hasta aproximadamente `161.06`, aunque se pierde información en las zonas que quedan saturadas en blanco.

La transformación de bajo contraste `0.5x + 64` comprime los valores al intervalo 64–191. Los extremos de la escala desaparecen y los niveles se concentran en una zona intermedia, por lo que la imagen presenta menor separación entre regiones claras y oscuras.

La transformación de alto contraste `2x − 128` separa más los niveles de intensidad. Los valores negativos se recortan a 0 y los superiores a 255, produciendo una imagen con mayor diferencia entre sombras y luces, pero también con posible saturación.

En la imagen a color se aplicó corrección gamma con `gamma = 0.5` a los canales B, G y R. La fórmula utilizada fue:

```text
y = 255 · (x / 255)^gamma
```

El notebook compara la imagen original y la transformada, además de mostrar para cada canal el histograma original, el histograma transformado y la capa resultante.

## Conclusiones

El taller muestra que una transformación de intensidad puede mejorar o modificar una imagen, pero cada operación produce efectos diferentes. La ecualización global redistribuye los niveles; el ajuste de brillo desplaza la intensidad media; el contraste modifica la separación entre niveles; y la corrección gamma aplica una transformación no lineal.

El uso de `np.clip` es necesario porque las fórmulas de aclaramiento y contraste pueden producir valores fuera del rango permitido por una imagen de 8 bits. El recorte mantiene la representación válida, pero puede generar saturación y pérdida de detalle en los extremos.

La comparación de histogramas permite verificar estos efectos de manera objetiva. Por ejemplo, el oscurecimiento desplaza la distribución hacia valores pequeños, el bajo contraste la comprime y el alto contraste la expande hacia los extremos.

Finalmente, aplicar gamma por canal demuestra que las transformaciones también pueden realizarse sobre imágenes a color. En este caso, cada componente se transforma de forma independiente, por lo que la apariencia final depende de cómo se redistribuyen las intensidades azul, verde y roja.

## Estructura

```text
taller3/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   └── paisaje.png
├── resultados/
│   ├── imagen_ecualizada.png
│   ├── histogramas_ecualizados.png
│   ├── imagen_oscurecida_pt3.png
│   ├── imagen_aclarada_pt4.png
│   ├── imagen_bajo_contraste_pt5.png
│   ├── imagen_alto_contraste_pt6.png
│   ├── gamma_color_pt7.png
│   └── canales_gamma_pt7.png
├── preguntas.md
├── readme.md
└── taller3.ipynb
```

## Librerías utilizadas

- `OpenCV` (`cv2`) para cargar imágenes, ecualizar histogramas y calcular frecuencias.
- `NumPy` (`numpy`) para aplicar fórmulas, normalizar valores y limitar intensidades.
- `Matplotlib` (`matplotlib.pyplot`) para visualizar imágenes e histogramas.
- `os` para crear la carpeta de resultados.
