from sys import stderr
from typing import List


def get_user_input():
    """Processes user input from standart input stream"""
    try:
        return [int(i) for i in input().split()]
    except ValueError as ve:
        print(ve, file=stderr)


def cummulative_sums(numbers: List[int]) -> List[int]:
    """Calculates the cummulative sum"""
    return [sum(numbers[:i]) for i in range(len(numbers) + 1)]


if __name__ == "__main__":
    data = get_user_input()
    print(cummulative_sums(data))
