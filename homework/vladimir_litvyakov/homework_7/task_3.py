result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'
result_4 = 'результат: 2'


def results(result_num):
    print(int(result_num.split(': ')[-1]) + 10)


results(result_1)
results(result_2)
results(result_3)
results(result_4)
