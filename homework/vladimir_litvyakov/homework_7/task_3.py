result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'
results_list = [result_1, result_2, result_3, result_4]


def results(result_num):
    print(int(result_num.split(': ')[-1]) + 10)


for result in results_list:
    results(result)
