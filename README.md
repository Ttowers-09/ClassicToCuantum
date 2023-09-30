# Números complejos

## Libreria NUMPY
La libreria Numpy también pronunciada Numpai es una biblioteca de lenguaje natural de Python, el cuál da soporte a la 
creación de vectores y matrices, junto a estas, una serie de operadores matemáticos

## Libreria MATH
la libreria Math es una biblioteca de lenguaje natural Python, da al usuario la disposición y uso de las operaciones algebraicas

## ¿Qué es Pycharm y para que sirve?
Pycharm es el IDE más popular para el lenguaje de programación python.

## Como instalar la libreria numpy en Pycharm
Para poder descargar la libreria debemos hacer los siguientes pasos:

    -Abrir Pychar y crear un nuevo documento.
    - Vamos al aportado de "File" y luego a la opción de "New projects settings"
	- Se desplegará una ventana y daremos click en "Project interpreter", damos clic en la flecha donde dice 
		"Add interpreter"
	- Buscaremos el nombre de nuestro proyecto y daremos click.
	- En la parte superior izquierda aparecerá un + le daremos click y en la barra buscaremos "Numpy"
	- Daremos click y luego en la parte inferior derecha un boton en verde que dice "Add package"
	- Esperaremos que cargue y listo ya quedó la libreria instalada en nuestro entorno de programación.
	- Para importar la función escribimos "import Numpy as np" y podremos disponer de la funciones de la libreria.
## Como instalar la libreria math en Pycharm
Para poder descargar la libreria debemos hacer los siguientes pasos:
	
    - Abrir Pychar y crear un nuevo documento.
	- Vamos al aportado de "File" y luego a la opción de "New projects settings"
	- Se desplegará una ventana y daremos click en "Project interpreter", damos clic en la flecha donde dice 
		"Add interpreter"
	- Buscaremos el nombre de nuestro proyecto y daremos click.
	- En la parte superior izquierda aparecerá un + le daremos click y en la barra buscaremos "math lab"
	- Daremos click y luego en la parte inferior derecha un boton en verde que dice "Add package"
	- Esperaremos que cargue y listo ya quedó la libreria instalada en nuestro entorno de programación.
	- Para importar la función escribimos "import math " y podremos disponer de la funciones de la libreria.

## Función "Complex" en python.
La función complex devuelve un número imaginario a partir de valores cedidios como argumentos.
La parte derecha de nuestro argumento se interpreta como parte imaginaria.
tupla (a,b) -> (a, bj)

## Función #1 "sistema_determinista"
Modelo matemático donde las mismas entradas o condiciones iniciales producirán invariablemente las mismas salidas o resultados, no contemplándose la existencia de azar, o incertidumbre en el proceso.

- Definimos un estado inicial en este caso "v".
- Definimos nuestros caminos en forma de matriz "m".
- Definimos la cantidad de "Clicks" que se le daran al estado.
- Realizamos el producto interno entre el estado inicial y nuestra matriz obteniendo como resultado un vector nuevo; este vector se almacenara en la variable "v" nuevamente.
- Se realizará este mismo proceso la cantidad de veces como de cliks tengamos definidos.

## Función #2 "sistema_probabilistico"
El sistema probabilístico es aquel en el que no se puede hacer una previsión detallada. Requiere de análisis más complejos para su estudio y la determinación de dichas probabilidades.

- Definimos un estado inicial en este caso "v2"
- Definimos nuestros caminos en forma de matriz "m2"
- Definimos la cantidad de "Clicks" que se le daran al estado.
- Realizamos el producto interno entre el estado inicial y nuestra matriz obteniendo como resultado un vector nuevo; este vector se almacenara en la variable "v" nuevamente.
- Se realizará este mismo proceso la cantidad de veces como de cliks tengamos definidos.

## Función #3 "sistema_cuantico"
A diferencia de los estados que hemos mencionado anteriormente este sistema incorpora la posibilidad de operaciones no conmutativas que tienen en cuenta tanto los estados cuánticos como los clásicos.
- Definimos un estado inicial en este caso "v3"
- Definimos nuestros caminos en forma de matriz "m3"
- Definimos la cantidad de "Clicks" que se le daran al estado.
- Realizamos el producto interno entre el estado inicial y nuestra matriz obteniendo como resultado un vector nuevo; este vector se almacenara en la variable "v" nuevamente.
- Se realizará este mismo proceso la cantidad de veces como de cliks tengamos definidos.

## Como se deben ejecutar las pruebas.
Las pruebas se deben ejecetar primero llamando la libreria unitest, a partir de ahi seguimos el procedimiento de llamar 
nuesta función de la libreria pasada. a partir de ahi definimos nuestras variables a utilizar y el valor que deseamos 
esperar, definimos la operación y al final citamos "np.testing.assert_almost_equal (operación, valor esperado)"

## Contacto
En caso de encontrar un "bug", error de programación o sugerencia favor comunicarse con Ivan Torres - ivan.forero-t@mail.escuelaing.edu.co