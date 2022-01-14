# Дано несколько чисел. Вычислите их сумму.
# Сначала вводите количество чисел N, затем вводится ровно N целых чисел.
def input_int(msg):
    """
    Ввод числа типа int

    :param msg: сообщение при вводе
    """
    print(msg, end="")
    while True:
        inp = input()
        if inp.isnumeric():
            return int(inp)
        print("Введено нецелое или не число!\nВведите заново: ", end="")


N = int(input("Введите число N: "))
numbers_sum = 0
for i in range(N):
    numbers_sum += int(input(f"Введите {i}-ое число: "))
