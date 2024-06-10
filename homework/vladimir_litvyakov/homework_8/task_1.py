import random


salary = random.randrange(80000, 150000)
bonus_bool = random.choice([True, False])
bonus_true = random.randrange(1000, 50000)
result = salary + bonus_true


if bonus_bool is True:
    print(f"{salary}, {bonus_bool} - '${result}'")
else:
    print(f"{salary}, {bonus_bool} - '${salary}'")
