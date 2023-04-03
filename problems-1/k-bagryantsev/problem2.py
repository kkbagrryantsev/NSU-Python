from collections.abc import Iterable
from sys import stderr


def get_user_input() -> List[int]:
    """Processes user input from standart input stream"""
    try:
        return [int(i) for i in input().split()]
    except ValueError as ve:
        print(ve, file=stderr)


def trim_numbers(inf: int, sup: int, numbers: Iterable[int]) -> Iterable[int]:
    """Replaces all integers out of range with lower or upper bound respectively"""
    return [inf if i < inf else (sup if i > sup else i) for i in numbers]


if __name__ == "__main__":
    infimum = int(input())
    supremum = int(input())
    data = get_user_input()
    print(trim_numbers(infimum, supremum, data))
