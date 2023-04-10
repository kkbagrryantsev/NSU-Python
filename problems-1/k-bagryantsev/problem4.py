NUMBERS = {1: "one",
           2: "two",
           3: "three",
           4: "four",
           5: "five",
           6: "six",
           7: "seven",
           8: "eight",
           9: "nine",
           10: "ten"}

def bottles(_state: int) -> str:
    while _state > 0:
        yield f'{NUMBERS[_state].capitalize()} green bottle{"s" if _state != 1 else ""} hanging on the wall'
        yield f'{NUMBERS[_state].capitalize()} green bottle{"s" if _state != 1 else ""} hanging on the wall'
        yield "And if one green bottle should accidentally fall"
        _state -= 1
        if _state == 0:
            continue
        yield f'There’ll be {NUMBERS[_state]} green bottle{"s" if _state != 1 else ""} hanging on the wall'
    else:
        yield "There’ll be no green bottles hanging on the wall"


if __name__ == '__main__':
    state = 10
    for i in bottles(state):
        print(i)
