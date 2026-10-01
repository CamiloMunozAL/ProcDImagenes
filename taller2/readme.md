# Taller 2 – Histogramas de imágenes

Este repositorio contiene el desarrollo del **Taller 2 de Procesamiento Digital de Imágenes**, enfocado en la construcción y análisis de histogramas para imágenes en escala de grises y para los canales de una imagen a color.

## Contenido

El taller desarrolla los siguientes puntos:

1. Cálculo del histograma de una imagen en escala de grises usando `cv2.calcHist`.
2. Cálculo y representación de los histogramas de los canales de una imagen a color.
3. Construcción manual de un vector de 256 posiciones para contar las frecuencias de los niveles de gris.
4. Graficación del histograma a partir del vector construido con ciclos.
5. Repetición del conteo manual para cada canal de una imagen a color: azul, verde y rojo.

## Concepto principal

Un histograma representa la distribución de intensidades de una imagen. El eje horizontal contiene los niveles posibles de intensidad, de 0 a 255, y el eje vertical indica cuántos píxeles poseen cada nivel.

En una imagen en escala de grises se utiliza un solo histograma. En una imagen a color se calcula un histograma independiente para cada canal. Como OpenCV carga la imagen en el orden **BGR**, el notebook trabaja con los canales azul, verde y rojo en las posiciones 0, 1 y 2, respectivamente.

## Resultados y análisis

La imagen utilizada tiene dimensiones de `533 × 800` píxeles, por lo que contiene `426400` píxeles. La suma de las frecuencias del histograma en escala de grises coincide con esta cantidad, lo que verifica que todos los píxeles fueron contabilizados.

El histograma calculado con `cv2.calcHist` y el histograma construido manualmente tienen la misma interpretación: cada una de las 256 posiciones del vector representa la frecuencia de un nivel de intensidad. El conteo manual permite comprender el funcionamiento interno del histograma, mientras que `calcHist` ofrece una solución más directa y optimizada.

Para la imagen a color, cada canal también contiene `426400` valores, porque cada píxel aporta una intensidad a cada una de las tres capas. Los histogramas separados permiten observar cómo se distribuye la información azul, verde y roja, y pueden revelar qué colores predominan en la escena.

## Conclusiones

El taller demuestra que el histograma es una herramienta útil para describir una imagen sin analizar individualmente su posición espacial. Permite identificar concentraciones de píxeles oscuros, claros o intermedios y sirve como base para técnicas posteriores como la ecualización y el ajuste de contraste.

La implementación manual mediante ciclos confirma que un histograma se obtiene recorriendo la imagen y aumentando el contador asociado al valor de cada píxel. La validación de que la suma de frecuencias coincide con el número total de píxeles demuestra que el procedimiento fue realizado correctamente.

El análisis por canales amplía esta idea a imágenes a color: en lugar de una única distribución, se estudia una distribución para cada componente. Esta separación será utilizada en el Taller 3 para aplicar transformaciones de intensidad a imágenes en color.

## Estructura

```text
taller2/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   └── paisaje.png
├── resultados/
│   ├── histogramapt1.png
│   ├── histogramacolorpt2.png
│   ├── histogramapt3y4.png
│   ├── histogramas_horizontal.png
│   └── histogramacolorpt5.png
├── preguntas.md
├── readme.md
└── taller2.ipynb
```

## Librerías utilizadas

- `OpenCV` (`cv2`) para cargar imágenes y calcular histogramas.
- `Matplotlib` (`matplotlib.pyplot`) para representar las frecuencias.
- `os` para crear la carpeta de resultados cuando es necesario.
