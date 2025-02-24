def choice_operation(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second and (first > 0 and second > 0):  # для выполнения операции "*" по ТЗ
            operation = '-'
        elif second > first and (first > 0 and second > 0):  # для выполнения операции "*" по ТЗ
            if second == 0:
                return "На ноль делить нельзя"
            else:
                operation = '/'
        elif (first < 0 or second < 0) and (first > 0 or second > 0):  # по ТЗ "Одно из чисел"
            operation = '*'
        else:
            return 'Неизвестная операция'

        return func(first, second, operation)
    return wrapper


@choice_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


user_input_1 = float(int(input("Введите первое число: ")))
user_input_2 = float(int(input("Введите второе число: ")))

print(calc(user_input_1, user_input_2))
