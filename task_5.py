
print('\nЗадание №5 \n**** Сумма чисел из строки ****')


def sum_str():
    result = 0
    continue_cycle = True
    while continue_cycle:
        str_numbers = []
        list_numbers = []
        input_string = input('Введите строку чисел, разделенных пробелом. '
                             'Для завершения введите "/": ')
        # ищем в строке символ остановки
        pos_end = input_string.find('/')
        # если найден - это последний цикл, обрезаем строку
        if pos_end >= 0:
            continue_cycle = False
            input_string = input_string[:pos_end]

        str_numbers = input_string.strip().split(' ')

        # если строка не пустая
        if len("".join(str_numbers)):
            try:
                # на случай, если было переданно не числовое значение
                list_numbers = list(map(float, str_numbers))
            except ValueError:
                print('Вы ввели значения, не являющиеся числами')
                return

            result += sum(list_numbers)

        print(f'Сумма введённых чисел: {result}')


sum_str()
