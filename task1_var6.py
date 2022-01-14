def input_by_pattern(pattern: str, message):
    """
    Ввод символа с проверкой на попадание в шаблон

    :param pattern: шаблон
    :param message: сообщение при вводе
    :return: символ, попадающий в шаблон
    """
    print(message, end="")
    pattern = list(pattern)
    while True:
        inp = input()
        if pattern.__contains__(inp):
            print("Координата успешно введена!")
            return inp
        print("Ошибка! Координата не удовлетворяет диапазону\nВведите заново:", end=" ")


def is_correct_queen_move(queen_horiz: int, queen_vert: int, dest_horiz: int, dest_vert: int):
    """
    Проверка корректности ходя ферзя относительно выполнения корректности хода ладьи и слона

    :param queen_horiz: горизонталь клетки ферзя
    :param queen_vert: вертикаль клетки ферзя
    :param dest_horiz: горизонталь клетки-цели
    :param dest_vert: вертикаль клетки-цели
    """
    is_correct_rook_move = queen_horiz == dest_horiz or queen_vert == dest_vert
    is_correct_bishop_move = abs(queen_vert - dest_vert) == abs(queen_horiz - dest_horiz)
    return is_correct_rook_move or is_correct_bishop_move


def substring_number_in_string(s: str, sub: str):
    """
    Номер подстроки в строке

    :param s: строка
    :param sub: подстрока
    """
    return s.index(sub) + 1


horizontal_coordinates = 'abcdefgh'
vertical_coordinates = '12345678'

msg_input_horizontal = f"Введите букву горизонтали клетки (диапазон: {horizontal_coordinates}): "
msg_input_vertical = f"Введите цифру вертикали клетки (диапазон: {vertical_coordinates}): "

print("Ввод координат клетки, где стоит ферзь")
queen_horiz_coord = input_by_pattern(horizontal_coordinates, msg_input_horizontal)
queen_vert_coord = input_by_pattern(vertical_coordinates, msg_input_vertical)

print("\nВвод координат клетки, куда должен попасть ферзь одним ходом")
dest_horiz_coord = input_by_pattern(horizontal_coordinates, msg_input_horizontal)
dest_vert_coord = input_by_pattern(vertical_coordinates, msg_input_vertical)

print("Ферзь сможет одним ходом попасть из первой клетки во вторую"
      if is_correct_queen_move(substring_number_in_string(horizontal_coordinates, queen_horiz_coord),
                               int(queen_vert_coord),
                               substring_number_in_string(horizontal_coordinates, dest_horiz_coord),
                               int(dest_vert_coord))
      else "Ферзь не сможет одним ходом попасть из первой клетки во вторую")
