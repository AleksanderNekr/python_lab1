from itertools import product


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


def square_monte_carlo(X, Y, a, b, c, d, e):
    """
    Нахождение площади многоугольника с прямыми углами через некоторые его стороны с помощью метода Монте-Карло

    :return: площадь многоугольника
    """
    rectangle_square = X * max(Y, e)
    correct_point_counts = 0
    all_points_count = 10000
    for _ in range(all_points_count):
        from random import random
        # координата x от 0 до max(Y, e)
        x = random() * max(Y, e)
        # координата y от 0 до X
        y = random() * X

        # Многоугольник разбивается на 3 прямоугольника:
        # нижний (со сторонами e и d)
        # средний (со сторонами Y - b и c)
        # верхний (со сторонами Y и a)
        is_in_bottom_square = x <= e and y <= d
        is_in_middle_square = x <= Y - b and d <= y <= d + c
        is_in_top_square = x <= Y and X - a <= y <= X
        if is_in_top_square or is_in_middle_square or is_in_bottom_square:
            correct_point_counts += 1
    return rectangle_square * correct_point_counts / all_points_count


print("Принято ограничение на натуральные числа для вычисления сторон фигуры!")
X = input_natural("Введите сторону Х: ")
Y = input_natural("Введите сторону Y: ")
Z = input_natural("Введите сторону Z: ")

# Так как a + c + d = X и e - Z + b = Y, то e + b = Z + Y,
# отсюда a + b + c + d + e = X + Y + Z, тогда периметр фигуры = (X + Y + Z) * 2
perimeter = (X + Y + Z) * 2

iter_count = 0
# Для упрощения записи вложенных циклов используется product из модуля itertools
for e, b in product(range(1, Z + Y), range(1, Z + Y)):
    if e + b == Z + Y and e > Z:
        for a, c, d in product(range(1, X), range(1, X), range(1, X)):
            if a + c + d == X:
                iter_count += 1
                print(f"{iter_count}-й случай: a = {a}, b = {b}, c = {c}, d = {d}, e = {e},"
                      f" площадь примерно равна: {square_monte_carlo(X, Y, a, b, c, d, e)}, периметр равен {perimeter}")
if iter_count == 0:
    print('Фигура не существует при заданных параметрах Х, Y и Z!')
