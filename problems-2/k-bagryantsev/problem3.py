import sys
from operator import itemgetter
from os import listdir, stat
from os.path import isfile


def print_dir_files(dirpath: str) -> None:
    """Prints all dir files' name & size pairs.
    Files are sorted by their size in descending order
    and by name in ascending order.

    Link to the documentation, which guarantees maintaining relative order of equal elements:
    https://docs.python.org/3.11/library/functions.html#sorted"""
    try:
        files = filter(isfile, listdir(dirpath))
        files = [(file, stat(file).st_size) for file in files]
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit("Expected a path to a directory.")
    print(*sorted(sorted(files, key=itemgetter(0)), key=itemgetter(1), reverse=True))


if __name__ == '__main__':
    print_dir_files(sys.argv[1])
