def input_int(msg):
    """
    Ввод числа типа int

    :param msg: сообщение при вводе
    """
    print(msg, end="")
    while True:
        inp = input()
        try:
            return int(inp)
        except ValueError:
            print("Введено нецелое или не число!\nВведите заново: ", end="")


def input_natural(msg):
    """
    Ввод натурального числа

    :param msg: сообщение при вводе
    """
    print(msg, end="")
    while True:
        inp = input()
        try:
            if int(inp) < 0:
                print("Количество чисел должно быть неотрицательным!\nВведите заново:", end=" ")
            else:
                return int(inp)
        except ValueError:
            print("Введено нецелое или не число!\nВведите заново: ", end="")


N = input_natural("Введите число N: ")
numbers_sum = 0
for i in range(N):
    numbers_sum += input_int(f"Введите {i + 1}-ое число: ")
print(f"Сумма чисел: {numbers_sum}")
