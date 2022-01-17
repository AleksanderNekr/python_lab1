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
