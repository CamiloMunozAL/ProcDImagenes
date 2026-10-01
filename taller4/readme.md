# Taller 4 – Procesamiento Digital de Imágenes

Este repositorio contiene el desarrollo del **Taller 4 de Procesamiento Digital de Imágenes**, enfocado en vecindad de píxeles, ecualización local y operaciones lógicas sobre imágenes.

## Contenido

El taller desarrolla los siguientes puntos:

1. Obtención de los **8 vecinos** de un píxel a partir de sus coordenadas.
2. Prueba del algoritmo de vecindad sobre una imagen en escala de grises.
3. Evaluación de vecindades específicas sobre `PIANO.bmp`.
4. Aplicación de **ecualización local** y comparación de histogramas.
5. Implementación manual de la ecualización local mediante ciclos, usando:
   - `Amin = 0.5`
   - `Amax = 2.5`
6. Implementación mediante ciclos de operaciones lógicas entre imágenes binarias:
   - AND
   - OR
   - XOR
   - NOT

## Conceptos principales

El taller relaciona tres ideas importantes del procesamiento digital de imágenes:

- **Vecindad:** análisis de los píxeles que rodean a una posición determinada.
- **Procesamiento local:** transformación de un píxel usando estadísticas calculadas en una ventana cercana.
- **Operaciones lógicas:** combinación píxel a píxel de imágenes binarias.

La vecindad utilizada es la de 8 píxeles, organizada en una matriz de `3 × 3`. El centro representa el píxel seleccionado y se marca con `-1`, porque no forma parte de sus propios vecinos.

## Resultados y análisis

### Vecindad de 8 píxeles

La función `obtener_8_vecinos(imagen, x, y)` valida que el píxel no se encuentre en el borde. Esto es necesario porque un píxel ubicado en una esquina o en un extremo no tiene ocho vecinos completos.

En la prueba realizada sobre `paisaje.png`, el píxel ubicado en `(100, 100)` tuvo intensidad `128` y se obtuvo la siguiente matriz:

```text
[[157, 124, 127],
 [167,  -1, 134],
 [169, 126, 135]]
```

La función también se probó sobre `PIANO.bmp` en las coordenadas `(82,29)`, `(68,27)`, `(112,89)`, `(114,89)` y `(27,130)`. Las zonas donde los vecinos tienen valores parecidos corresponden a regiones homogéneas; las diferencias grandes entre vecinos indican posibles bordes o cambios de textura.

### Ecualización local

La ecualización local utiliza una ventana de `3 × 3` para calcular la media y la desviación estándar alrededor de cada píxel. La transformación aplicada es:

```text
y(i,j) = A(i,j) · (x(i,j) − media_local) + media_local
```

Cuando una región tiene poco contraste, el factor de realce puede aumentar para hacer visibles sus detalles; cuando ya existe mucha variación local, el realce es menor. Los valores resultantes se limitan al rango `[0, 255]` mediante `np.clip`.

### Ecualización local manual

La segunda implementación repite el procedimiento mediante ciclos explícitos. Para cada píxel interno se calcula la ventana, la media, la desviación estándar y el nuevo valor transformado. El factor se limita al intervalo `0.5 ≤ A(i,j) ≤ 2.5`.

Según los valores registrados en el notebook, el promedio de intensidad pasó de `72.14` a `71.69`. Además, la cantidad de píxeles saturados en 0 disminuyó de más de `20.000` en la primera versión a `185` en la versión manual limitada. Esto muestra que controlar el factor de realce reduce modificaciones excesivas y conserva mejor la distribución original.

### Operaciones lógicas

Antes de aplicar las operaciones, las imágenes `CuadroBinGrande.pgm` y `CuadroBinChico.pgm` se convierten a imágenes binarias con valores 0 y 255. Las operaciones se implementan recorriendo cada píxel:

- **AND:** conserva las regiones blancas presentes en ambas imágenes.
- **OR:** conserva las regiones blancas presentes en al menos una de las imágenes.
- **XOR:** conserva las regiones donde las imágenes son diferentes.
- **NOT:** invierte cada píxel, convirtiendo 0 en 255 y 255 en 0.

Las imágenes deben tener el mismo tamaño para aplicar AND, OR y XOR, porque cada píxel de una imagen se combina con la posición equivalente de la otra.

## Conclusiones

El análisis de vecinos demuestra que la información de una imagen no depende únicamente del valor aislado de un píxel. Las diferencias entre sus vecinos permiten reconocer regiones uniformes, bordes y cambios de textura.

La ecualización local aprovecha esa información espacial para mejorar el contraste de forma diferente en cada zona. Sin embargo, un factor de realce sin límites puede producir saturación. La implementación manual con `Amin` y `Amax` ofrece un resultado más controlado y estable.

Las operaciones lógicas permiten crear máscaras, combinar regiones e invertir imágenes binarias. En conjunto, el taller conecta vecindad, procesamiento local y operaciones binarias, conceptos importantes para filtrado, detección de bordes, segmentación y análisis de objetos.

## Estructura

```text
taller4/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   ├── paisaje.png
│   ├── PIANO.bmp
│   ├── PIANO.pgm
│   ├── CuadroBinGrande.pgm
│   └── CuadroBinChico.pgm
├── resultados/
│   ├── punto1.png
│   ├── ecualizacion_local_pt4.png
│   ├── ecualizacion_local_manual_pt5.png
│   └── operaciones_logicas_pt6.png
├── preguntas.md
├── readme.md
└── taller4.ipynb
```

## Librerías utilizadas

- `OpenCV` (`cv2`) para cargar imágenes, convertirlas a escala de grises, binarizarlas y calcular histogramas.
- `NumPy` (`numpy`) para construir matrices, calcular estadísticas locales y limitar intensidades.
- `Matplotlib` (`matplotlib.pyplot`) para visualizar imágenes, píxeles seleccionados e histogramas.
- `os` para crear la carpeta de resultados.
