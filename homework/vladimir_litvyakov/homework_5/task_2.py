result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'


result_1_slice = int(result_1[20:]) + 10
result_1_index = int(result_1.index('42')) + 10
print(result_1_slice)
print(result_1_index)


result_2_slice = int(result_2[20:]) + 10
result_2_index = int(result_2.index('514')) + 10
print(result_2_slice)
print(result_2_index)


result_3_slice = int(result_3[28:]) + 10
result_3_index = int(result_3.index('9')) + 10
print(result_3_slice)
print(result_3_index)
