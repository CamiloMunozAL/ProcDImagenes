# Taller 8 – Detección de puntos, líneas y bordes

Este repositorio contiene el desarrollo del **Taller 8 de Procesamiento Digital de Imágenes**. El taller estudia la segmentación y la detección de características mediante máscaras espaciales, gradientes, umbrales y ciclos implementados en Python.

## Enlaces

- [Carpeta del Taller 8 en GitHub](https://github.com/CamiloMunozAL/ProcDImagenes/tree/main/taller8)
- [Cuaderno Python del Taller 8](https://github.com/CamiloMunozAL/ProcDImagenes/blob/main/taller8/taller8.ipynb)

## Contenido

Se desarrollan siete ejercicios:

1. Detección de puntos aislados.
2. Detección de líneas horizontales, verticales y diagonales.
3. Detección de bordes con el operador Prewitt.
4. Detección de bordes con el operador Sobel.
5. Detección de bordes con el operador Laplaciano.
6. Detección de bordes con Marr-Hildreth.
7. Detección de bordes con una implementación manual de Canny.

## Imágenes utilizadas

El taller utiliza imágenes sintéticas de puntos, líneas y un cuadrado, además de:

- `images/CampoEstrellas.png`
- `images/paisaje.png`

Estas imágenes permiten probar los detectores sobre estructuras simples, estrellas y escenas naturales.

## Métodos implementados

### Puntos y líneas

El detector de puntos aislados utiliza una máscara espacial para identificar píxeles cuya intensidad difiere significativamente de sus vecinos. También se analiza el efecto de eliminar el factor `1/9` de la máscara.

La detección de líneas utiliza máscaras orientadas para resaltar estructuras horizontales, verticales y diagonales.

### Prewitt y Sobel

Prewitt y Sobel calculan gradientes en las direcciones horizontal y vertical. La magnitud del gradiente permite localizar cambios rápidos de intensidad asociados con bordes.

### Laplaciano

El operador Laplaciano utiliza derivadas de segundo orden para resaltar cambios de intensidad en distintas direcciones. Puede responder con intensidad a bordes y detalles, pero también al ruido.

### Marr-Hildreth

Marr-Hildreth combina un suavizado Gaussiano con el Laplaciano y localiza bordes mediante cruces por cero. El informe también compara resultados con distintos umbrales.

### Canny

La implementación manual de Canny utiliza `sigma=5` e incluye:

- Cálculo del gradiente.
- Magnitud y dirección del gradiente.
- Supresión de no máximos.
- Doble umbral.
- Histéresis para conectar bordes fuertes y débiles.

## Resultados

Los resultados se guardan en la carpeta `results` e incluyen:

- Detección de puntos aislados y estrellas.
- Comparación de la detección de estrellas.
- Detección de líneas.
- Resultados de Prewitt, Sobel y Laplaciano.
- Resultados de Marr-Hildreth y sus umbrales intermedios.
- Resultados de Canny sobre el cuadrado y el paisaje.
- Comparación de diferentes umbrales para Canny.

## Conclusiones

Las máscaras espaciales permiten identificar estructuras específicas a partir de las variaciones locales de intensidad. Los detectores de puntos y líneas son útiles cuando se conoce la orientación o el tipo de característica buscada.

Prewitt y Sobel permiten detectar bordes mediante gradientes. Sobel da mayor peso a los vecinos cercanos y suele producir respuestas más robustas frente a pequeñas variaciones.

El Laplaciano detecta cambios mediante derivadas de segundo orden, aunque puede ser más sensible al ruido. Marr-Hildreth reduce parte de esta sensibilidad mediante un suavizado previo y la búsqueda de cruces por cero.

Canny combina varias etapas para obtener bordes más definidos y conectados. El resultado depende de los umbrales seleccionados, por lo que no existe una configuración única adecuada para todas las imágenes.

## Ejecución

El desarrollo principal se encuentra en `taller8.ipynb`:

1. Abrir el notebook desde la carpeta `taller8`.
2. Ejecutar las celdas en orden.
3. Verificar que las imágenes de entrada estén en `images`.
4. Consultar los resultados generados en `results`.

El informe LaTeX se encuentra en `doc/main.tex`. Para compilarlo, se debe ejecutar la compilación desde `taller8/doc`, ya que las imágenes se referencian mediante rutas relativas a `../results`.

## Estructura

```text
taller8/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   ├── CampoEstrellas.png
│   └── paisaje.png
├── results/
│   ├── canny_comparacion_umbrales.png
│   ├── deteccion_bordes_canny_cuadrado.png
│   ├── deteccion_bordes_canny_paisaje.png
│   ├── deteccion_bordes_laplaciano.png
│   ├── deteccion_bordes_marr_hildreth.png
│   ├── deteccion_bordes_prewitt.png
│   ├── deteccion_bordes_sobel.png
│   ├── deteccion_estrellas_comparacion.png
│   ├── deteccion_lineas.png
│   ├── deteccion_puntos_aislados.png
│   ├── deteccion_puntos_estrellas.png
│   └── marr_hildreth_umbrales_intermedios.png
├── readme.md
└── taller8.ipynb
```

## Librerías utilizadas

- `NumPy` (`numpy`) para operaciones numéricas y procesamiento con máscaras.
- `OpenCV` (`cv2`) para cargar imágenes y aplicar algunas operaciones de procesamiento.
- `Matplotlib` (`matplotlib.pyplot`) para visualizar y guardar los resultados.
- `os` para crear y administrar la carpeta de resultados.