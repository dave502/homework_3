print('\nЗадание №3 \n**** Сумма двух максимальных значений ****')


def my_func(var1, var2, var3):
    """Возвращает сумму двух максимальных аргументов

    :param var1: int or float
    :param var2: int or float
    :param var3: int or float
    :return: float
    """
    numeric_list = []

    try:
        # на случай, если было переданно не числовое значение
        numeric_list = list(map(float, [var1, var2, var3]))
    except ValueError:
        print('Вы ввели значения, не являющиеся числами')
        return

    # сортируем список по возрастанию и суммируем второе и третье значение, исключая наименьшее
    return sum(sorted(numeric_list, reverse=True)[:2])


print(my_func(9.6, 6, '8'))