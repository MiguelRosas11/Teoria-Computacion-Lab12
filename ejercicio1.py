"""Ordena una lista de diccionarios por la clave indicada."""

from argparse import ArgumentParser
from json import loads
from pprint import pprint


TELEFONOS = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Apple", "model": 2, "color": "Silver"},
    {"make": "Huawei", "model": 50, "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]


def ordenar_diccionarios(diccionarios, clave):
    return sorted(diccionarios, key=lambda diccionario: diccionario[clave])


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("clave", nargs="?", default="model")
    parser.add_argument("diccionarios", nargs="?", type=loads, default=TELEFONOS)
    args = parser.parse_args()

    if not isinstance(args.diccionarios, list) or any(
        not isinstance(diccionario, dict) for diccionario in args.diccionarios
    ):
        parser.error("Se esperaba una lista JSON de objetos.")

    try:
        pprint(ordenar_diccionarios(args.diccionarios, args.clave), sort_dicts=False)
    except KeyError:
        parser.error(f"La clave {args.clave!r} debe existir en cada diccionario.")
    except TypeError:
        parser.error(f"Los valores de la clave {args.clave!r} deben poder compararse.")
