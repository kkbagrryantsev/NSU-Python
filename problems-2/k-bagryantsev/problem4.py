from collections.abc import Iterator
from sys import stderr


class StringFinder(Iterator):
    """Instantiates an iterator over all entries of a substring in a string.
    Includes overlapping cases.

    :string -- string to be searched through
    :substring -- string to be searched for
    """
    def __init__(self, string, substring):
        self._string = string
        self._substring = substring
        self._ptr = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._ptr < len(self._string):
            self._ptr = self._string.find(self._substring, self._ptr + 1)
            if self._ptr == -1:
                raise StopIteration()
            return self._ptr


def findall(string: str, substring: str) -> list[int]:
    """Counts all substring occurences in given string including overlaping ones.

    :argument string -- string to be searched through
    :argument substring -- substring to be found
    """
    finder = StringFinder(string, substring)
    return [i for i in finder]


if __name__ == '__main__':
    try:
        _substring = input()
    except Exception as e:
        print(e)
        exit("Expected a string sequence of numbers.")

    try:
        with open("pi.txt") as pi:
            _result = findall(pi.read()[2:], _substring)
            print(f"Found {len(_result)} results.")
            print(f"Positions:", *_result[:5], "...")
    except Exception as e:
        print(e, file=stderr)
        exit("Check pi.txt is in current working directory and is not corrupted.")
