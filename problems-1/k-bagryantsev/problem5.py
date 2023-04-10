from math import sqrt, ceil
from typing import Any, Generator


def is_prime(a: int) -> bool:
    for _i in range(2, ceil(sqrt(a))):
        if a % _i == 0:
            return False
    return True


def eratosthenes_sieve(_divisor: int) -> Generator[int, Any, None]:
    while _divisor := _divisor + 1:
        if is_prime(_divisor):
            yield _divisor


def factorizate_number(a: int) -> dict:
    divisors = dict()
    divisor = 2
    sieve = eratosthenes_sieve(divisor)
    while divisor <= a:
        while a % divisor == 0:
            if divisors.get(divisor) is None:
                divisors[divisor] = 0
            divisors[divisor] += 1
            a //= divisor
        divisor = next(sieve)
    return divisors


if __name__ == '__main__':
    num = int(input())
    result = factorizate_number(num)
    print([(key, value) for key, value in result.items()])
