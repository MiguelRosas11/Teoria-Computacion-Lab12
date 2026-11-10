"""Elimina de una lista las apariciones de los elementos indicados."""

from argparse import ArgumentParser
from json import loads


COLORES = ["rojo", "verde", "azul", "amarillo", "gris", "blanco", "negro"]
COLORES_A_BORRAR = ["amarillo", "café", "blanco"]


def eliminar_elementos(elementos, a_borrar):
    return list(filter(lambda elemento: elemento not in a_borrar, elementos))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("elementos", nargs="?", type=loads, default=COLORES)
    parser.add_argument("a_borrar", nargs="?", type=loads, default=COLORES_A_BORRAR)
    args = parser.parse_args()

    if not isinstance(args.elementos, list) or not isinstance(args.a_borrar, list):
        parser.error("Se esperaban dos listas JSON.")

    print(eliminar_elementos(args.elementos, args.a_borrar))
