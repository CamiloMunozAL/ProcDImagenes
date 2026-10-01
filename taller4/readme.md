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
│   └── imágenes generadas durante el taller
├── preguntas.md
└── taller4.ipynb