from collections.abc import Iterable
from math import ceil, sqrt
from sys import stderr


def primes(bound: int) -> Iterable[int]:
    """Calculates all prime numbers less than specified bound using Eratosthenes sieve.

    :argument bound -- positive integer bound
    """
    if bound < 0:
        raise ValueError("Negative number")
    if bound < 2:
        return []

    result = [True] * (bound + 1)
    result[0] = False
    result[1] = False

    for i in range(2, ceil(sqrt(bound))):
        if result[i]:
            for j in range(i ** 2, bound, i):
                result[j] = False

    return [index for index, value in enumerate(result) if value]


if __name__ == '__main__':
    try:
        _n = int(input())
        print(*primes(_n))
    except Exception as e:
        exit(f"{e}\nExpected a positive integer")
