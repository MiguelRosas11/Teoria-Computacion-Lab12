# Laboratorio No. 12 · Teoría de la Computación

Cuatro ejercicios de programación en Python con funciones lambda. Los programas
usan la biblioteca estándar de Python 3.

## Ejecutar los ejemplos del enunciado

Desde la raíz del repositorio, ejecuta estos comandos. En Windows también
puedes usar `py` en lugar de `python`.

```sh
python ejercicio1.py
python ejercicio2.py
python ejercicio3.py
python ejercicio4.py
```

| Ejercicio | Qué hace la función lambda | Resultado del ejemplo |
| --- | --- | --- |
| 1. Ordenar diccionarios | Extrae de cada diccionario el valor asociado a la clave que usa `sorted`. | Devuelve los teléfonos Apple, Samsung, Huawei y Nokia con sus datos completos. |
| 2. Calcular potencias | Eleva cada entero al exponente positivo con `map`. | `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]` |
| 3. Transponer una matriz | Construye una fila de salida con los elementos de una columna de entrada. | `[[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 0, -1]]` |
| 4. Eliminar elementos | Usa `filter` para conservar los elementos que no figuran en la lista de borrado. | `['rojo', 'verde', 'azul', 'gris', 'negro']` |

## Probar otras entradas

Escribe las listas como JSON. Los ejemplos de abajo usan comillas simples
alrededor de cada argumento JSON y comillas dobles dentro de él.

```sh
python ejercicio1.py color
python ejercicio2.py 2 '[-3, 0, 4]'
python ejercicio3.py '[[1, 2, 3]]'
python ejercicio4.py '[1, 2, 1, 3, 4]' '[1, 4, 9]'
```

- **Ordenar** requiere que todos los diccionarios tengan la clave elegida y que
  sus valores se puedan comparar entre sí. Si dos valores son iguales, sus
  diccionarios conservan el orden original.
- **Potencias** admite bases negativas y cero. El exponente debe ser un entero
  mayor que cero.
- **Transponer** admite matrices cuadradas y rectangulares. Todas las filas
  deben tener la misma longitud. Una matriz vacía o sin columnas devuelve `[]`.
- **Eliminar** conserva el orden, quita todas las apariciones de cada elemento
  indicado e ignora los elementos de borrado que no están en la lista original.

Los cuatro programas aceptan una lista de entrada vacía y devuelven `[]`.

## Video de ejecución

Pendiente de publicar en YouTube como video no listado.
