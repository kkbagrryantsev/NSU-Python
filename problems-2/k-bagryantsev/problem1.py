from collections.abc import Iterable
from math import ceil, sqrt
from time import time


def gcd(_a: int, _b: int) -> int:
    """Calculates greatest common divisor using Euclidean algorithm.

    :argument _a -- integer
    :argument _b -- integer
    :return -- greatest common divisor
    """
    if _a % _b == 0:
        return _b
    return gcd(_b, _a % _b)


def pythagorean_triple(_n: int) -> Iterable[(int, int, int)]:
    """Enumerates all pythagorean triples with element no more than given bound.

    :argument _n -- upper bound for triple elements
    :return -- iterable collection of triples
    """
    return [(x, y, z)
            for x in range(1, _n + 1)
            for y in range(x, _n + 1)
            for z in range(y, _n + 1)
            if x ** 2 + y ** 2 == z ** 2]


def pythagorean_triple2(bound: int) -> Iterable[(int, int, int)]:
    """Enumerates all pythagorean triples with element no more than given bound.
    Calculates triples via Euclidean formula.

    :argument bound -- upper bound for triple elements
    :return -- iterable collection of triples
    """
    return [(*sorted(((m ** 2 - n ** 2) * k, 2 * m * n * k, z)),)
            for m, n in [(m, n)
                         for n in range(1, ceil(sqrt(bound)) + 1)
                         for m in range(n + 1, ceil(sqrt(bound)) + 1)
                         if gcd(m, n) == 1 and (m - n) % 2 != 0]
            for k in range(1, bound)
            if (z := (m ** 2 + n ** 2) * k) <= bound]


if __name__ == '__main__':
    _bound = int(input())
    _start = time()
    print(*pythagorean_triple2(_bound))
    print(f"[TIME] {time() - _start}")
    _start = time()
    print(*pythagorean_triple(_bound))
    print(f"[TIME] {time() - _start}")
