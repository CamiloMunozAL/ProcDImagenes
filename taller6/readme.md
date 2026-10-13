# Taller 6 – Espectro de imágenes y Transformada Discreta de Fourier

Este repositorio contiene el desarrollo del **Taller 6 de Procesamiento Digital de Imágenes**, enfocado en la representación de imágenes en el dominio de la frecuencia mediante la Transformada Discreta de Fourier bidimensional (DFT 2D).

## Enlaces

- [Carpeta del Taller 6 en GitHub](https://github.com/CamiloMunozAL/ProcDImagenes/tree/main/taller6)
- [Cuaderno Python del Taller 6](https://github.com/CamiloMunozAL/ProcDImagenes/blob/main/taller6/taller6.ipynb)

## Contenido

El taller desarrolla los siguientes puntos:

1. Implementación directa de la DFT 2D mediante cuatro ciclos anidados.
2. Visualización de los espectros de magnitud con centrado de frecuencias y escala logarítmica.
3. Implementación de la DFT 2D aprovechando la propiedad de separabilidad mediante transformadas unidimensionales.
4. Comparación numérica y temporal entre la implementación directa, la implementación separable y `np.fft.fft2`.

## Imágenes de prueba

Se utilizaron cuatro imágenes sintéticas de `64x64` píxeles para facilitar la interpretación de los espectros y evitar tiempos excesivos de procesamiento:

- Cuadrado blanco de `32x32` sobre fondo negro.
- Círculo blanco de radio 16 sobre fondo negro.
- Franjas verticales blancas y negras.
- Imagen uniforme con intensidad 128.

Las imágenes se generan directamente con NumPy y se visualizan en `results/imagenes_sinteticas.png`.

## Conceptos principales

La DFT 2D transforma una imagen del dominio espacial al dominio de la frecuencia. Para una imagen `f(x,y)` de tamaño `M x N`, cada coeficiente `F(u,v)` se calcula considerando todos los píxeles de la imagen:

$$
F(u,v)=\frac{1}{MN}
\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}
f(x,y)e^{-i2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
$$

El espectro de magnitud permite analizar la distribución de frecuencias espaciales. Las frecuencias bajas se ubican cerca del centro después de aplicar `np.fft.fftshift`, mientras que las frecuencias altas aparecen más alejadas.

Debido a que los coeficientes pueden tener magnitudes muy diferentes, se utiliza la escala logarítmica:

$$
S(u,v)=\ln\left(1+\left|F_c(u,v)\right|\right)
$$

donde `F_c(u,v)` representa la transformada con las frecuencias centradas.

## Implementación directa

La DFT directa utiliza cuatro ciclos anidados. Los dos ciclos exteriores recorren las frecuencias `(u,v)` y los dos interiores recorren todos los píxeles `(x,y)` de la imagen.

Para una imagen cuadrada de tamaño `M x N`, este procedimiento requiere aproximadamente:

$$
O(M^2N^2)
$$

Aunque sigue directamente la definición matemática, su costo aumenta rápidamente con el tamaño de la imagen.

## Propiedad de separabilidad

La DFT 2D puede calcularse mediante dos DFT unidimensionales sucesivas, aplicando primero la transformación sobre las filas y después sobre las columnas. Esto es posible porque:

$$
e^{-i2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}
=
e^{-i2\pi\frac{ux}{M}}
\cdot
e^{-i2\pi\frac{vy}{N}}
$$

La implementación separable reduce el costo aproximado a:

$$
O(MN^2+NM^2)
$$

En las pruebas realizadas con imágenes de `64x64`, la DFT directa tardó aproximadamente `16,80` segundos por imagen, mientras que la versión separable tardó cerca de `0,49` segundos. Los resultados fueron numéricamente equivalentes, con diferencias máximas del orden de `10^{-13}`.

## Interpretación de los resultados

- El cuadrado produce componentes asociadas con sus bordes horizontales y verticales.
- El círculo genera una distribución espectral aproximadamente radial.
- Las franjas verticales concentran sus componentes en el eje asociado con la variación horizontal.
- La imagen uniforme presenta principalmente la componente continua, porque no contiene variaciones espaciales.

El centrado del espectro y la escala logarítmica facilitan la observación de componentes que podrían quedar ocultas por las grandes diferencias de magnitud entre los coeficientes.

## Resultados

- `results/imagenes_sinteticas.png`: imágenes de entrada utilizadas en el taller.
- `results/espectros_dft.png`: imágenes originales y sus espectros de Fourier centrados en escala logarítmica.

## Ejecución

El desarrollo principal se encuentra en `taller6.ipynb`. Para ejecutarlo:

1. Abrir el notebook desde la carpeta `taller6`.
2. Ejecutar las celdas en orden.
3. Esperar el cálculo de la DFT directa, que puede tardar varios segundos por imagen.
4. Consultar las imágenes generadas en `results`.

El informe en LaTeX se encuentra en `doc/main.tex`. La compilación debe ejecutarse desde `taller6/doc`, porque las imágenes se referencian mediante rutas relativas a `../results`.

## Estructura

```text
taller6/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   └── paisaje.png
├── results/
│   ├── espectros_dft.png
│   └── imagenes_sinteticas.png
├── readme.md
└── taller6.ipynb
```

## Librerías utilizadas

- `NumPy` (`numpy`) para crear las imágenes, calcular sumatorias y realizar operaciones con matrices complejas.
- `Matplotlib` (`matplotlib.pyplot`) para visualizar y guardar las imágenes y los espectros.
- `time` para medir los tiempos de ejecución de las implementaciones.