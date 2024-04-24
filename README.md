# Resolución del Cubo de Rubik - Reporte Técnico
## 1. Autor:
Daho Fabio Copa Mejia

## 2. Descripción del Proyecto

El proyecto tiene como objetivo resolver el famoso rompecabezas del Cubo de Rubik utilizando técnicas de programación. Se implementará un programa en Python que cargará el estado del cubo desde un archivo de texto y aplicará algoritmos para encontrar la solución como el BFS.

## 3. Requerimientos del Entorno de Programación

- Python 3.x
- Bibliotecas estándar de Python

## 4. Manual de Uso
### 4.1 Formato de Codificación para Cargar el Estado del Cubo desde el Archivo de Texto

El archivo de texto (configuracion_cubo.txt) debe seguir el siguiente formato:

W W W
W W W
W W W
O O O 
R R R 
G G G 
B B B
O O O 
R R R 
G G G 
B B B
O O O 
R R R 
G G G 
B B B
Y Y Y
Y Y Y
Y Y Y

Es como hacer:

      W W W
      W W W
      W W W
O O O R R R G G G B B B
O O O R R R G G G B B B
O O O R R R G G G B B B
      Y Y Y
      Y Y Y
      Y Y Y

Donde cada letra representa el color de una cara del cubo:

- W: Blanco
- O: Naranja
- R: Rojo
- G: Verde
- B: Azul
- Y: Amarillo

Cada bloque de 3 líneas representa una cara del cubo.
### 4.2 Instrucciones para Ejecutar el Programa

- Clona este repositorio de GitHub
- Abre una terminal y navega hasta el directorio del proyecto.
- Ejecuta el programa con el comando: python3 cubo_rubik.py.

## 5. Diseño e Implementación
### 5.1 Modelo del Problema

El problema del Cubo de Rubik es un rompecabezas mecánico tridimensional que consta de 6 caras, cada una dividida en 9 cuadrados de colores. El objetivo es resolver el cubo de manera que cada cara tenga un solo color. El cubo tiene aproximadamente 43 quintillones de posibles configuraciones, lo que lo convierte en un problema desafiante para resolver de manera eficiente.

### 5.2 Algoritmos, Técnicas, Heurísticas Seleccionadas

Se ha implementado un algoritmo basado en la búsqueda primero en anchura (BFS) para encontrar la solución al cubo de Rubik. Además, se utiliza la heurística de la distancia de Manhattan para estimar la distancia al estado objetivo y guiar la búsqueda.

De primeras se quizo realizar el algoritmo (BFS), se tubo algunos problemas y no se llego a implementar, es una caracteristica que le falta, solo se llego a la validacion del cubo ademas de sus movimientos, ademas de la realizacion de este documento.

### 5.3 Modelos Lingüísticos Utilizados

Se ha usado para validar ciertas funciones y hacer una revicion del codigo, Ejm: Esta funcion esta bien hecha, que me recomiendas hacer para corregir, etc. Una ayuda para no estancarse con errores o bugs.

## 6. Trabajo Futuro
### 6.1 Tareas Inconclusas e Ideas para Continuar con el Proyecto

- Implementar algoritmos como A* o el BFS.
- Agregar una interfaz gráfica para una experiencia de usuario más interactiva.
- Optimizar el código para mejorar el rendimiento y la legibilidad (Refactorizar).