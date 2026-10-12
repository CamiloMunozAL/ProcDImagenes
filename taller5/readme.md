# Taller 5 – Filtrado espacial de imágenes

Este repositorio contiene el desarrollo del **Taller 5 de Procesamiento Digital de Imágenes**, enfocado en la implementación de filtros espaciales sobre una imagen en escala de grises. Los filtros se construyen mediante ciclos y operaciones de vecindad para estudiar el suavizado, la reducción de ruido y el realce de bordes.

## Enlaces

- [Cuaderno Python del Taller 5](https://github.com/CamiloMunozAL/ProcDImagenes/blob/main/taller5/taller5.ipynb)
- [Carpeta del Taller 5 en GitHub](https://github.com/CamiloMunozAL/ProcDImagenes/tree/main/taller5)

## Contenido

El taller desarrolla los siguientes puntos:

1. Aplicación de filtros paso bajo de promedio con tres máscaras:
   - Máscara uniforme de `3x3`.
   - Máscara uniforme de `5x5`.
   - Máscara ponderada de `3x3`.
2. Implementación de filtros de media de `3x3` y `5x5`.
3. Implementación de filtros de mediana de `3x3` y `5x5`.
4. Aplicación de filtros paso alto con máscaras de `3x3` y `5x5`.
5. Comparación entre aplicar directamente un filtro paso alto y aplicarlo después de un filtro de mediana.

## Imagen utilizada

Para todos los ejercicios se utiliza `images/paisaje.png`, una fotografía en escala de grises que contiene montañas, árboles, vegetación, cielo, agua y reflejos. La variedad de regiones uniformes, bordes y texturas permite observar las diferencias entre los filtros.

La imagen se carga con OpenCV utilizando `cv2.IMREAD_GRAYSCALE`. Sus intensidades se representan normalmente en el intervalo de 0 a 255.

## Conceptos principales

El filtrado espacial calcula un nuevo valor para cada píxel a partir de una vecindad local. Una máscara o núcleo se desplaza sobre la imagen y sus coeficientes determinan cómo se combinan los píxeles vecinos.

### Filtros paso bajo

Los filtros paso bajo atenúan las variaciones rápidas de intensidad y producen suavizado o desenfoque. En el taller se comparan:

- **Promedio uniforme:** todos los píxeles de la ventana tienen el mismo peso.
- **Promedio ponderado:** el píxel central y sus vecinos cercanos tienen mayor influencia.
- **Media:** calcula el promedio aritmético de la vecindad.
- **Mediana:** ordena los valores de la ventana y selecciona el valor central. Es un filtro no lineal y puede reducir ruido impulsivo conservando algunos bordes.

En general, una ventana `5x5` suaviza más que una ventana `3x3`, pero también puede eliminar una mayor cantidad de detalles. La máscara ponderada `3x3` suele conservar mejor los bordes que la máscara uniforme del mismo tamaño.

### Filtros paso alto

Los filtros paso alto resaltan cambios bruscos de intensidad, por lo que permiten visualizar bordes, texturas y detalles finos. Las respuestas pueden ser negativas o superar el rango válido de una imagen de 8 bits; por ello, para visualizarlas se utiliza la magnitud absoluta y se limita el resultado con `np.clip`.

En las pruebas realizadas, el filtro paso alto `5x5` produjo respuestas más intensas que el filtro `3x3`:

- Respuesta máxima absoluta `3x3`: `1214`.
- Respuesta máxima absoluta `5x5`: `3802`.
- Píxeles con magnitud superior a 255 en `3x3`: `21808`.
- Píxeles con magnitud superior a 255 en `5x5`: `152985`.

Estos valores explican las regiones saturadas en blanco que aparecen al visualizar el resultado del filtro `5x5`.

### Tratamiento de los bordes

En los filtros paso bajo se procesan las posiciones que permiten utilizar una ventana completa y se conservan los bordes originales. En el filtro paso alto, la imagen de salida se inicializa con ceros, por lo que las posiciones exteriores que no se procesan permanecen en cero.

## Resultados y análisis

El promedio uniforme `3x3` produce un suavizado moderado, mientras que la ventana uniforme `5x5` genera un desenfoque más evidente. El promedio ponderado `3x3` asigna más importancia al centro de la máscara y conserva mejor algunos contornos del paisaje.

Los filtros de media generan un suavizado progresivo al aumentar el tamaño de la ventana. El filtro de mediana produce cambios relativamente leves en esta imagen y mantiene buena parte de los contornos principales, aunque puede eliminar detalles finos.

Los filtros paso alto hacen visibles los bordes de las montañas, los árboles, la vegetación y los reflejos del agua. Las regiones uniformes, como algunas zonas del cielo y del lago, presentan respuestas bajas.

Al aplicar primero un filtro de mediana y después un filtro paso alto, se reducen algunas variaciones pequeñas y ciertas texturas. Como resultado, algunos bordes principales se distinguen con mayor facilidad que cuando se aplica el paso alto directamente sobre la imagen original. Sin embargo, este procedimiento también puede eliminar información fina, por lo que la elección depende del objetivo del procesamiento.

## Conclusiones

El taller muestra que no existe un filtro universalmente mejor: cada técnica responde a una necesidad distinta.

- Los filtros de promedio y media son útiles para suavizar, aunque pueden reducir detalles.
- El promedio ponderado conserva mejor algunos bordes al dar mayor peso al centro.
- La mediana ofrece un suavizado no lineal y puede conservar contornos importantes.
- Los filtros paso alto permiten destacar bordes y texturas, pero requieren controlar valores negativos y saturación.
- Combinar mediana y paso alto puede facilitar la identificación de bordes principales al reducir variaciones pequeñas previamente.

La implementación mediante ciclos permite comprender directamente la relación entre la máscara, la vecindad y el nuevo valor asignado a cada píxel.

## Ejecución

El desarrollo principal se encuentra en el notebook `taller5.ipynb`. Para ejecutarlo:

1. Abrir `taller5.ipynb` desde la carpeta `taller5`.
2. Ejecutar las celdas en orden.
3. Verificar que la imagen de entrada se encuentre en `images/paisaje.png`.
4. Consultar las imágenes generadas en la carpeta `results`.

El notebook crea la carpeta `results` automáticamente si no existe.

El informe en LaTeX se encuentra en `doc/main.tex`. Para compilarlo, la compilación debe ejecutarse desde `taller5/doc`, ya que las imágenes se referencian mediante rutas relativas a `../results`.

## Estructura

```text
taller5/
├── doc/
│   ├── main.tex
│   └── main.pdf
├── images/
│   ├── imgpt1.png
│   └── paisaje.png
├── results/
│   ├── resultado_filtro_mediana.png
│   ├── resultado_filtro_media.png
│   ├── resultado_filtro_paso_alto.png
│   ├── resultado_filtro_promedio.png
│   └── resultado_mediana_paso_alto.png
├── readme.md
└── taller5.ipynb
```

## Librerías utilizadas

- `OpenCV` (`cv2`) para cargar la imagen en escala de grises.
- `NumPy` (`numpy`) para representar imágenes, construir máscaras, realizar cálculos y limitar intensidades.
- `Matplotlib` (`matplotlib.pyplot`) para visualizar y guardar los resultados.
- `os` para crear la carpeta de resultados.
