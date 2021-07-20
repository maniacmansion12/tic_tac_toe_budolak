def show_2():
    print()
    print(f"  | 1 | 2 | 3 |")
    print("---------------")
    print(f"1 | {field_1[11]} | {field_1[12]} | {field_1[13]} |")
    print("---------------")
    print(f"2 | {field_1[21]} | {field_1[22]} | {field_1[23]} |")
    print("--------------")
    print(f"3 | {field_1[31]} | {field_1[32]} | {field_1[33]} |")
    print("---------------")
    print()


def ask_1():
    while True:
        xy = input("         Ваш ход: ")

        if len(xy) != 2:
            print(" Введите 2 координаты без пробела! ")
            continue

        if not (xy.isdigit()):
            print(" Введите числа! ")
            continue

        xy = int(xy)

        if xy not in field_1:
            print(" Координаты вне диапазона! ")
            continue

        if field_1[xy] != " ":
            print(" Клетка занята! ")
            continue

        return xy


def check_win():
    if field_1[11] == field_1[12] == field_1[13] != " ":
        print(f"Победили {field_1[11]}!!!")
        show_2()
        return True
    elif field_1[21] == field_1[22] == field_1[23] != " ":
        print(f"Победили {field_1[21]}!!!")
        show_2()
        return True
    elif field_1[31] == field_1[32] == field_1[33] != " ":
        print(f"Победили {field_1[31]}!!!")
        show_2()
        return True
    elif field_1[11] == field_1[21] == field_1[31] != " ":
        print(f"Победили {field_1[11]}!!!")
        show_2()
        return True
    elif field_1[12] == field_1[22] == field_1[32] != " ":
        print(f"Победили {field_1[12]}!!!")
        show_2()
        return True
    elif field_1[13] == field_1[23] == field_1[33] != " ":
        print(f"Победили {field_1[13]}!!!")
        show_2()
        return True
    elif field_1[11] == field_1[22] == field_1[33] != " ":
        print(f"Победили {field_1[11]}!!!")
        show_2()
        return True
    elif field_1[13] == field_1[22] == field_1[31] != " ":
        print(f"Победили {field_1[13]}!!!")
        show_2()
        return True

    return False


def greet():
    print("-------------------")
    print(" Добро пожаловать  ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: xy  ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print()
    print()


num = 0
field_1 = {11: ' ', 12: ' ', 13: ' ', 21: ' ', 22: ' ', 23: ' ', 31: ' ', 32: ' ', 33: ' '}
greet()
while True:
    num += 1
    show_2()

    if num % 2 != 0:
        print("Ходят крестики")
        print()
    else:
        print("Ходят нолики")
        print()

    xy = ask_1()
    if num % 2 != 0:
        field_1[xy] = "X"
    else:
        field_1[xy] = "O"

    if check_win():
        break

    if num == 9:
        print("ничья")
        show_2()
        break