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


all_points_count = input_natural("Введите точность вычисления площади методом Монте-Карло (рекомендуется 100 000): ")
square = 8 * 4
shape_points_count = 0
for i in range(all_points_count):
    # координата x от 0 до 8
    x = random.random() * 8
    # координата y от 4 до 8
    y = random.random() * 4 + 4
    is_in_triangle = y <= x * 0.5 + 4
    is_in_rectangle = 5 <= x <= 7 and 5 <= y <= 6
    if is_in_triangle and not is_in_rectangle:
        shape_points_count += 1
print(f"Площадь примерно равна {square * shape_points_count / all_points_count}")
