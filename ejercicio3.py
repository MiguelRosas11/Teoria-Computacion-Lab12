"""Transpone una matriz rectangular representada como lista de listas."""

from argparse import ArgumentParser
from json import loads


MATRIZ = [[1, 2, 3, 1], [4, 5, 6, 0], [7, 8, 9, -1]]


def transponer(matriz):
    if not matriz:
        return []

    ancho = len(matriz[0])
    if any(len(fila) != ancho for fila in matriz):
        raise ValueError("Todas las filas deben tener la misma longitud.")

    return list(map(lambda columna: [fila[columna] for fila in matriz], range(ancho)))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("matriz", nargs="?", type=loads, default=MATRIZ)
    args = parser.parse_args()

    if not isinstance(args.matriz, list) or any(
        not isinstance(fila, list) for fila in args.matriz
    ):
        parser.error("Se esperaba una lista JSON de listas.")

    try:
        print(transponer(args.matriz))
    except ValueError as error:
        parser.error(str(error))
