def collatz_conjecture_trace(a: int) -> str:
    trace = [str(a)]
    while a != 1:
        a = a // 2 if a % 2 == 0 else 3 * a + 1
        trace.append(str(a))
    return "->".join(trace)


if __name__ == '__main__':
    number = int(input())
    print(collatz_conjecture_trace(number))
