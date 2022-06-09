"""
Aprendizaje de este curso
-Entender el concepto e importancia de estrucutras de datos
-Comprender el comportamiento, uso e implementación de estructuras de datos lineales con python
-Poner en practica lo aprendido

porque Python ?
--sintaxis clara
-- semántica clara
-- Escalable
-- Interactivo
-- Proposito General
-- Gratis y popular


Elementos de la programación en Python
 -- elementos léxicos -> if, while, def, etc
convenciones
    variable
    CONSTANTES
    nombre_funcion
    nombreClase

A tomar en cuenta
sintaxis
Literales
Operadores
import
Condicionales
Loops

Estructuras propias
-Listas
-Tuplas
-Conjuntos (sets)
-Diccionarios


funciones
Declaración y llamada
Recursivas
Anidadas
High order function
Lambdas


-------- Tipos de Colecciones(estrucuturas de datos)-------
Que es una coleccion
 -es un conjunto 0  grupo de cero o mas elementos que pueden tratarse como una unidad conceptual

 Cero o más elementos ?
        los datos pueden tener distintas representaciones, None != 0 -> 0 es un valor numero None = Nada
Tipos de colecciones:
    - Dinámicas(crecer o dosminuir su tamaño)
    - Inmutables(que son aquellas que no van a cambiar)

 ----- Colecciones Lineales(listas, pilas y colas) ----
 .Ordenadas por posición
 .Solo el primer elemento No tiene Predecesor

  D1->D2->D3->D4->D5

  ejemplos(de estructuras de datos lineales):
    - Fila en el supermercado
    - Pila de platos
    - Checklist

---- Colecciones Jerárquicas ---
    . Ordenadas como un árbol invertido
    . Solo el primer eleemento No tiene predecesor
    .Padres e Hijos.

    ejemplos(de estructuras de daots Jerarquics)
    - libros, Capítulos, Temas
    -  Abuelos, Madres, Hijo

--- Colecciones Grafos ----
 . Cada dato puede tener varios predecesores y sucesores
 . Estos se llaman vecinos

 ejemplos(de estructuras grafos)
    - Vuelos aéreos, sistemas de recomendación
    - La mismísima internet es un grafo


----------------------------------------- Estructuras Desordenadas ------------------------
Estructuras como Bolsa, Bolsa ordenada, Conjuntos, DIccionarios, Diccionario ordenados.
.No tienen orden en particular
.No hay predecesores o sucesores.
    Ejemplo
    Una bolsa de gomitas, no sabe de qué color te va a tocar.

------------------------------------  Estructuras Ordenadas --------------------------------
Son estructuras que imponen un orden con una regla. Generalmente una regla de orden.
item <= item(i+1) Es decir que el tiem que sigue es el primer elemento +1.
Ej:
Los directorios telefónicos, los catálogos,

colecciones lineales -> listas, pilas y colas
colecciones no lineales -> Arboles, grafos


------------------------------------ Operaciones Esenciales en colecciones -----------
- Tamaño ->  conocer su tamañano
. Pertenencia -> para conocer la pertenencia de un elemento, si es que se encuentra dentro de esa colecion
. Recorrido -> recorrer dicha coleccion, cada uno de sus elementos
. String -> convertirlo o representarlo como string algunos de sus elementos o la coleccion complenta
. igualdad -> si dos colecciones son iguales
. concatenacion -> cuando unimos o sumamos listas o diccionarios
. Conversión de tipo -> podemos convertir de un tipo de coleccion a otro(no es tan comun)
. Insertar -> insertar elementos, al principio, al final, o una posicion determinada
. Remover -> .... lo mismo pero con remover
.Reemplazar -> ... lo mismo pero con reemplazar
. Acceder -> .. lo mimso pero con acceder


------------------------------ Colecciones Incorporadas en Python ----------------------
Listas/List
    - proposito General
    - Estructura más utilizada
    - De tipo secuencial
    - Ordenable

Tuplas/Tuples
 - Inmutable(no se pueden añadir o cambiar)
 - Utiles para datos contantes
 - Más rápidas que las listas
 - Tipo secuencial

  Ejemplo:
    son utiles para los datos constantes, podemos pensar en un mapa, coordenadas, podemos usar tuplas, el domicilio, el numero de una casa

Conjuntos/Sets
 .Almacena objetos no-duplicados
 .De acceso rápido
 .Aceptan operaciones lógicas(conjucion, disyuccion, etc...)
 .Son desordenados

 Ejemplo:
    Estos almacena elementos o objetos que no son duplicados, por ejemplo una receta de cocina, estos ingredientes no se replican.

Diccionarios/ Dictionaries
    .Pares de llave/valor
    .Arrays asociativos
    .son desordenados

entonces : Una estructura de datos es la representación interna de una colección de información,


-------------------------------------------------------- ARRAYS -------------------------------------------------------
es la representación interna de una coleccion de información

conceptos clave:

elemento -> valor almacenado en las posiciones del array
indice -> referencia a la posicion del elemento

En a memoria los arrays se almacenan de manera consecutiva, los bits se guardan casilla por casilla consecutivamente. mientras que en una lista noooooooooooooo

El array tiene una capacidad de almacenamiento. Puedo tener arrays en 1,2 y/o 3 dimensiones. A mayor complejidad dimensional, es decir, si aumenta la dimensión se hace más complicado acceder a estos datos, se recomienda en python trabajar con dimensiones
dimensiones < 2

Nota: los arrays son un tipo de listas, pero las listas no son arrays. Los arrays son diferentes y poseen las sigueintes restricciones:
No pueden:
    Agregar posiciones -> es decir no crecen
    Remover Posiciones -> no se pueden remover posiciones
    Modificar su tamañano -> pues, si no se puede agregar posiciones o remover posiciones no se puede modificar el tamaño
    Su capacidad se define al crearse
los arrays se usan en los sprites de los videojuegos, o en un menú de opciones


Python cuenta con un modulo array pero no es tan versatil, ya que solo almacena numeros y caracteres



------------------------------------------------ Linked Structures ----------------------------

-Consiste de nodos conectados a otros
- Los más comunes son sencillos o dobles
- No se accede por indice, sino por recorrido

conceptos:
    Data : valor almacenado en nodos
    Next: referencia al siguiente nodo
    Previous: referencia al nodo anterior
    Head: referencia al primer nodo
    Tail: al ultimo nodo

Implementar otras estructuras
Optimización

head
[] -> [D1 | Referencia] -> [D2 | Referencia] -> [D3 | None]
[Tail] -> apunta D3

ejemplos: Historial de un navegador, Hacer/rehacer operaciiones en un
editor de texto

linked list

son estructuras de datos lineales, donde sus elementos no están almacenados
en bloques continuos de memoria, a diferencia de los array, que estos son almacenados
de bloques continuos de memoria, mientras que las Linked List son almacenados en diferentes
sectores de la memoria y hace referencia a sus elementos mediantes punteros


--------  Iterable ------

se le llama asi un objeto que es capaz de retornar sus miembros uno a la vez. Entres los
iterables se encuentran estrucutras de secuencia como son:
strings
listas
tuples


--- Iterador ----
Objeto que está representando un flujo de datos

Este iterador es bueno para dar un paseo sobre el conjunto de valores



-------------------- Circular Linked List(Lista Enlazada Circular) -----
En el primer elemento tiene un puntero que apunta al elemento final y elemento final
apunta al primero. Esto se traduciría en un bucle infinito, también se puede combinar
con las anteriores

------------------ Double linked list ----------------
un puntero  hace referencia al siguiente nodo y al anterior, en caso del primer nodo, esta solamente va hacer
referencia al primero

--- stackst -> pilas ------
.colección lineal
.Basados en arrays o linked list

el principio fundamental de los stacks es:
LIFO, es decir, que el ultimo elemento en entrar será el primero en salir

operaciones:
    -Añadir: push
    -Remover: pop
    -Top:conocer cual es el elemento superior
    -Bottom:elemento hasta abajo de la pila

    aplicaciones:
        -Invertir el orden de una lista
        -implementar "undo" -> control z
        -Mantener historiales
        -Backtracking : es decir, que tenemos informacion
        y queremos del final al principio

    stack vs list:
    Similares, no iguales
    List: append, pop.
    Es afectada por sus otros métodos

queues -> colas -> fifo
aquel elemento que llego primero a la fila va hcer el primero en salir
rear -> el ultimo elemento que entro
front -> esta hasta el frente, el primero que va hacer atendido
Priority queues-> se basa en Fifo con elementos de mayor/menor prioridad

por ejemplo: sus elementos pueden tener
una prioridad distinta al ser atendidas
quisas alguno de esos elementos intermedio va hacer atendido
mas rapido o antes que front, por ejemplo en el abordaje de un avion
hay personas que tienen un pase ejecutivo

en las colas de los hospitales de acuerdo al nivel de
urgencia de las personas, eso obviamente altera




"""