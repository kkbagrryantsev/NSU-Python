from operator import itemgetter
from sys import stderr


class BilingualDictionary(dict):
    """Bilingual dictionary class for origin - translations pairs.

    :argument -- contents of the dictionary
    """
    def __init__(self, contents: dict):
        super().__init__(contents)

    def inverted(self):
        """Inverts the dictionary to become image to domain dictionary."""
        _inverted = dict()
        for origin, translations in self.items():
            for translation in translations:
                _inverted[translation] = _inverted.get(translation, []) + [origin]
        return BilingualDictionary(_inverted)


if __name__ == '__main__':
    try:
        with open("dict.txt", "r") as file:
            _dict = dict()
            while record := file.readline():
                _key, _value = record.split(" - ")

                _origin = _key.strip()
                _translations = [_translation.strip() for _translation in _value.split(",")]

                _dict[_origin] = _translations
            _dictionary = BilingualDictionary(_dict)
    except OSError as e:
        print(e, file=stderr)
        exit("Tried to read the file dict.txt from current working directory.")
    except Exception as e:
        print(e, file=stderr)
        exit("Tried to deserialize a dictionary from a file. Expected a list of records: [origin] - [translations].")

    try:
        with open("inverted_dict.txt", "w") as file:
            _inverted_dictionary = _dictionary.inverted()
            records = sorted(_inverted_dictionary.items(), key=itemgetter(0, 1))
            file.writelines([key + " - " + ", ".join(value) + "\n" for key, value in records])
    except Exception as e:
        print(e, file=stderr)
        exit("Tried to write the inverted dictionary to inverted_dict.txt.")
