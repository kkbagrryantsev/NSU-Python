from collections.abc import Iterable
from math import ceil, sqrt


def primes(bound: int) -> Iterable[int]:
    """Calculates all prime numbers less than specified bound using Eratosthenes sieve."""
    if bound < 0:
        raise ValueError("Negative number")

    result = [True] * bound
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
        raise e
