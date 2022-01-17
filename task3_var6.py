import random


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


all_points_count = input_natural("Введите точность вычисления площади методом Монте-Карло: ")
square = 8 * 4
shape_points_count = 0
for i in range(all_points_count):
    x = random.uniform(0, 8)
    y = random.uniform(4, 8)
    is_in_triangle = y <= x * 0.5 + 4 and 0 <= x <= 8 and 4 <= y <= 8
    is_in_rectangle = 5 <= x <= 7 and 5 <= y <= 6
    if is_in_triangle and not is_in_rectangle:
        shape_points_count += 1
print(square * shape_points_count / all_points_count)
