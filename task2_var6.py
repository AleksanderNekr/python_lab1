def input_float(msg):
    """
    Ввод числа типа float

    :param msg: сообщение при вводе
    """
    print(msg, end="")
    while True:
        inp = input()
        try:
            return float(inp)
        except ValueError:
            print("Введено не число!\nВведите заново: ", end="")


def input_natural(msg):
    """
    Ввод натурального числа

    :param msg: сообщение при вводе
    """
    print(msg, end="")
    while True:
        inp = input()
        try:
            if int(inp) <= 0:
                print("Число должно быть положительным!\nВведите заново: ", end="")
            else:
                return int(inp)
        except ValueError:
            print("Введено нецелое или не число!\nВведите заново: ", end="")


N = input_natural("Введите количество чисел: ")
numbers_sum = 0
for i in range(N):
    numbers_sum += input_float(f"Введите {i + 1}-ое число: ")
print(f"Сумма чисел: {numbers_sum}")
