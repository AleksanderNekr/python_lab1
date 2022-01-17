def input_coordinate(msg):
    """
    Ввод координат клетки шахматной доски

    :param msg: сообщение, в котором указывается, что это за клетка
    :return: координаты клетки (тип – str)
    """
    is_correct_coord = False
    coord = ""
    while not is_correct_coord:
        coord = input(f"Введите координаты клетки, {msg} (например: а1): ").lower()
        if horiz_coords.__contains__(coord[0]) and vert_coords.__contains__(coord[1]):
            print("Координаты успешно введены!\n")
            is_correct_coord = True
        else:
            print("Координаты введены неверно! Введите заново")
            is_correct_coord = False
    return coord


def is_correct_queen_move(queen_horiz: int, queen_vert: int, dest_horiz: int, dest_vert: int):
    """
    Проверка корректности хода ферзя из клетки, где он находится, в клетку-цель

    :param queen_horiz: горизонталь клетки ферзя
    :param queen_vert: вертикаль клетки ферзя
    :param dest_horiz: горизонталь клетки-цели
    :param dest_vert: вертикаль клетки-цели
    """
    is_correct_rook_move = queen_horiz == dest_horiz or queen_vert == dest_vert
    is_correct_bishop_move = abs(queen_vert - dest_vert) == abs(queen_horiz - dest_horiz)
    return is_correct_rook_move or is_correct_bishop_move


horiz_coords = 'abcdefgh'
vert_coords = '12345678'

queen_coord = input_coordinate('где стоит ферзь')
dest_coord = input_coordinate('куда ферзь должен попасть одним ходом')

print(f"Ферзь сможет одним ходом попасть из {queen_coord} в {dest_coord}"
      if is_correct_queen_move(horiz_coords.index(queen_coord[0]) + 1, int(queen_coord[1]),
                               horiz_coords.index(dest_coord[0]) + 1, int(dest_coord[1]))
      else f"Ферзь не сможет одним ходом попасть из {queen_coord} в {dest_coord}")
