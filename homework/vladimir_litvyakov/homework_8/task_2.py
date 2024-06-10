import sys


sys.set_int_max_str_digits(1000000)


def fibonacci(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


def get_fibonacci_number(position):
    generator = fibonacci(position + 1)
    number = 0
    for _ in range(position):
        number = next(generator)
    return number


positions = [5, 200, 1000, 100000]
for pos in positions:
    print(f'{pos}-е число Фибоначчи: {get_fibonacci_number(pos)}')
