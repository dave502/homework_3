
print('\nЗадание №4 \n**** Возведение в степень ****')


def my_func(x: float, y: int):
    """Возведение в отрицательную степень (с помощью оператора **)

    :param x: float positive
    :param y: int negative
    :return: float
    """
    try:
        x = float(x)
        y = int(y)

        if (type(x) == float) & (x > 0) & (type(y) == int) & (y < 0):
            return x ** y
        else:
            print("Некорретный тип данных. Ожидаются действительное "
                  "положительное число x и целое отрицательное число y")
    except ValueError:
        print("Некорретный тип данных. Ожидаются действительное "
              "положительное число x и целое отрицательное число y")


print(my_func(5, '-3'))


def my_func1(x: float, y: int):
    """Возведение в отрицательную степень (с помощью цикла)

    :param x: float positive
    :param y: int negative
    :return: float
    """
    try:
        x = float(x)
        y = int(y)

        if (type(x) == float) & (x > 0) & (type(y) == int) & (y < 0):
            epx_x = x
            for i in range(abs(y) - 1):
                epx_x *= x
            return 1 / epx_x
        else:
            print("Некорретный тип данных. Ожидаются действительное "
                  "положительное число x и целое отрицательное число y")
    except ValueError:
        print("Некорретный тип данных. Ожидаются действительное "
              "положительное число x и целое отрицательное число y")


print(my_func1(5, '-3'))
