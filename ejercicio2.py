"""Eleva cada entero de una lista a la potencia n."""

from argparse import ArgumentParser
from json import loads


def elevar_enteros(enteros, n):
    if type(n) is not int or n <= 0:
        raise ValueError("El exponente debe ser un entero positivo.")
    return list(map(lambda entero: entero ** n, enteros))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("n", nargs="?", type=int, default=3)
    parser.add_argument("enteros", nargs="?", type=loads, default=list(range(1, 11)))
    args = parser.parse_args()

    if not isinstance(args.enteros, list) or any(
        type(entero) is not int for entero in args.enteros
    ):
        parser.error("Se esperaba una lista JSON de enteros.")

    try:
        print(elevar_enteros(args.enteros, args.n))
    except ValueError as error:
        parser.error(str(error))
