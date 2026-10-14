# Taller 7 – Filtrado de imágenes en el dominio de la frecuencia

Este repositorio contiene el desarrollo del **Taller 7 de Procesamiento Digital de Imágenes**, enfocado en el filtrado de imágenes mediante máscaras construidas en el dominio de la frecuencia.

Los filtros se implementan en Python utilizando ciclos para construir las máscaras y la Transformada Rápida de Fourier (`FFT`) para transformar y reconstruir las imágenes.

## Enlaces

- [Carpeta del Taller 7 en GitHub](https://github.com/CamiloMunozAL/ProcDImagenes/tree/main/taller7)
- [Cuaderno Python del Taller 7](https://github.com/CamiloMunozAL/ProcDImagenes/blob/main/taller7/taller7.ipynb)

## Contenido

El taller desarrolla seis filtros:

1. Filtro ideal paso bajo.
2. Filtro Butterworth paso bajo.
3. Filtro Gaussiano paso bajo.
4. Filtro ideal paso alto.
5. Filtro Butterworth paso alto.
6. Filtro Gaussiano paso alto.

Los filtros se prueban con diferentes frecuencias de corte y, en el caso de Butterworth, con distintos órdenes.

## Imágenes utilizadas

Se utilizaron tres imágenes en escala de grises:

- **Cuadrado:** imagen sintética de `256x256` píxeles con un cuadrado blanco de `128x128` sobre fondo negro.
- **Rostro:** fotografía con detalles de piel, ojos, cabello y contornos faciales.
- **Paisaje:** fotografía con montañas, árboles, vegetación y un lago con reflejos.

El cuadrado se genera con NumPy y las fotografías se cargan desde:

```text
images/rostro.png
images/paisaje.png
```

Las pruebas utilizan frecuencias de corte `20`, `40` y `80`.

## Fundamentos

El filtrado en frecuencia transforma la imagen mediante la FFT, multiplica su representación por una máscara `H(u,v)` y luego aplica la transformada inversa para reconstruir la imagen:

$$
G(u,v)=F(u,v)H(u,v)
$$

En esta expresión, `F(u,v)` es la transformada de la imagen, `H(u,v)` es la máscara del filtro y `G(u,v)` es la transformada filtrada.

### Filtro paso bajo

Un filtro paso bajo conserva las frecuencias cercanas al centro del espectro y atenúa las frecuencias altas. Por ello, suaviza la imagen y reduce detalles finos.

El filtro ideal paso bajo utiliza una transición abrupta:

$$
H_{LP}(u,v)=
\begin{cases}
1, & D(u,v)\leq D_0\\
0, & D(u,v)>D_0
\end{cases}
$$

donde `D(u,v)` es la distancia al centro del espectro y `D_0` es la frecuencia de corte.

### Filtro paso alto

El filtro paso alto atenúa las frecuencias bajas y conserva las altas, resaltando bordes, texturas y variaciones rápidas de intensidad. En el taller se construye como el complemento del filtro paso bajo:

$$
H_{HP}(u,v)=1-H_{LP}(u,v)
$$

Las respuestas paso alto pueden contener valores positivos y negativos. Para visualizarlas se utiliza la magnitud absoluta y se normaliza al intervalo de intensidades de la imagen.

### Filtro Butterworth

El filtro Butterworth permite controlar gradualmente la transición entre las frecuencias conservadas y atenuadas mediante la frecuencia de corte `D_0` y el orden `n`:

$$
H_{LP}(u,v)=
\frac{1}{1+\left(\frac{D(u,v)}{D_0}\right)^{2n}}
$$

Un orden bajo produce una transición más suave, mientras que un orden alto aproxima el comportamiento de un filtro ideal y puede favorecer la aparición de oscilaciones o anillado.

### Filtro Gaussiano

El filtro Gaussiano utiliza una transición gradual basada en una función exponencial:

$$
H_{LP}(u,v)=
\exp\left(
-\frac{D(u,v)^2}{2D_0^2}
\right)
$$

Su versión paso alto se obtiene mediante `1 - H_LP`. Debido a su transición suave, suele producir menos oscilaciones que los filtros ideal y Butterworth.

## Resultados y análisis

Los filtros paso bajo suavizan las imágenes al eliminar componentes de alta frecuencia. Con una frecuencia de corte baja, el cuadrado pierde definición, el rostro pierde detalles de la piel y el cabello, y el paisaje pierde texturas. Al aumentar la frecuencia de corte se recuperan progresivamente más detalles.

El filtro ideal presenta transiciones abruptas y puede generar halos u oscilaciones alrededor de los bordes. Butterworth permite controlar la suavidad de la transición mediante su orden; sin embargo, los órdenes altos pueden producir un comportamiento similar al ideal y generar anillado. El filtro Gaussiano presenta cambios más graduales y no muestra oscilaciones pronunciadas.

En los filtros paso alto, las frecuencias de corte bajas resaltan con mayor intensidad los contornos del cuadrado, el rostro y las estructuras del paisaje. Al aumentar la frecuencia de corte, la respuesta se vuelve más tenue porque se conservan menos componentes relevantes para los bordes principales.

La selección del filtro depende del objetivo:

- El ideal ofrece una separación clara, pero puede producir oscilaciones.
- Butterworth permite ajustar la transición mediante el orden.
- Gaussiano proporciona una transición suave y resultados más estables.

## Resultados generados

Las imágenes procesadas se guardan en la carpeta `results`:

- `filtro_ideal_paso_bajo.png`
- `filtro_butterworth_paso_bajo.png`
- `filtro_butterworth_varios_ordenes.png`
- `filtro_gaussiano_paso_bajo.png`
- `filtro_ideal_paso_alto.png`
- `filtro_butterworth_paso_alto.png`
- `filtro_butterworth_paso_alto_ordenes.png`
- `filtro_butterworth_paso_alto_zoom.png`
- `filtro_gaussiano_paso_alto.png`

## Ejecución

El desarrollo principal se encuentra en `taller7.ipynb`. Para ejecutarlo:

1. Abrir el notebook desde la carpeta `taller7`.
2. Ejecutar las celdas en orden.
3. Verificar que `images/rostro.png` y `images/paisaje.png` estén disponibles.
4. Consultar las imágenes generadas en `results`.

El notebook crea la carpeta `results` automáticamente si no existe.

El informe LaTeX se encuentra en `doc/main.tex`. Para compilarlo, la ejecución debe realizarse desde `taller7/doc`, ya que las imágenes se referencian mediante rutas relativas a `../results`.

## Estructura

```text
taller7/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   ├── paisaje.png
│   └── rostro.png
├── results/
│   ├── filtro_butterworth_paso_alto.png
│   ├── filtro_butterworth_paso_alto_ordenes.png
│   ├── filtro_butterworth_paso_alto_zoom.png
│   ├── filtro_butterworth_paso_bajo.png
│   ├── filtro_butterworth_varios_ordenes.png
│   ├── filtro_gaussiano_paso_alto.png
│   ├── filtro_gaussiano_paso_bajo.png
│   ├── filtro_ideal_paso_alto.png
│   └── filtro_ideal_paso_bajo.png
├── readme.md
└── taller7.ipynb
```

## Librerías utilizadas

- `NumPy` (`numpy`) para crear imágenes, construir máscaras y realizar operaciones numéricas.
- `OpenCV` (`cv2`) para cargar las fotografías en escala de grises.
- `Matplotlib` (`matplotlib.pyplot`) para visualizar y guardar los resultados.
- `os` para crear la carpeta de resultados.