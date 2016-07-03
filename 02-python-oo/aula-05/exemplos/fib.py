def fib():
    a, b = 0, 1
    while True:
        a, b = b, b + a
        yield b
