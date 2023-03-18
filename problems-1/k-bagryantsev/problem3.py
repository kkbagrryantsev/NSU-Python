def collatz_conjecture_trace(a: int) -> str:
    trace = [str(a)]
    while a != 1:
        a = (a % 2 == 0 and a // 2) or 3 * a + 1
        trace.append(str(a))
    return "->".join(trace)


if __name__ == '__main__':
    number = int(input())
    print(collatz_conjecture_trace(number))
