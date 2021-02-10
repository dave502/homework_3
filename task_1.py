
print('\nЗадание №1 \n************* Функция деления *************')


def division(dividend, divider):
    """Производит деление аргументов

    :param dividend: int or float - делимое
    :param divider: int or float - делитель
    :return: float - результат деления dividend / divider
    """
    try:
        dividend = float(dividend)
        divider = float(divider)

        if divider != 0:
            return dividend / divider
        else:
            print('На ноль делить нельзя')
        # или
        # try:
        #     return dividend / divider
        # except ZeroDivisionError:
        #     print('Ошибка! На ноль делить нельзя.')

    except ValueError:
        print('Вы ввели значения, не являющиеся числами')

    return


a = input('Введите число (делимое): ')
b = input('Введите число (делитель): ')
print(division(a, b))
