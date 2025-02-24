def repeat_me(func):
    def wrapper(text, count):
        for _ in range(count):
            func(text)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def repeat_me_v2(count):
    def inner_repeat(func):
        def wrapper(text):
            for _ in range(count):
                func(text)
        return wrapper
    return inner_repeat


@repeat_me_v2(count=2)
def example_2(text):
    print(text)


example_2('hello')
