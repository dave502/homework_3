
print('\nЗадание №6 \n**** Слова с заглавными буквами ****')


def int_func(in_string: str):
    """Возвращает слово с заглавной буквой

    :param in_string: str
    :return:  str
    """
    # удаляем лишние пробелы
    in_string = in_string.strip()

    if in_string.isalpha():
        return in_string.title()
    else:
        print("Введены некорректные данные")
        return None


print(int_func('JHJKJG'))

sentence = input('Введите предложение из нескольких слов: ')

next_word = True  # условие продолжения цикла
start_with = 0  # начало следующего слова
end_word = 0  # конец следующего слова
sentence = sentence.strip()  # удаляем лишние пробелы
new_sentence = ""  # переменная для нового предложения

while next_word:
    # ищем следующий пробел - конец слова, начиная с найденного предыдущего прибела
    end_word = sentence.find(' ', start_with)
    # если нашли - передаём слово перед пробелом в функцию
    if end_word >= 0:
        new_sentence += int_func(sentence[start_with:end_word].strip()) + ' '
        # следующий поиск пробела начнётся с позиции, следующей после найденного в этом цикле пробела
        start_with = end_word + 1
    # если не нашли - значит это последнее слово, заканчиваем цикл
    else:
        new_sentence += int_func(sentence[start_with:].strip())
        next_word = False

print(new_sentence)

# или более простой способ
# создаём список слов из предложения
words_list = [i.strip() for i in sentence.split(' ')]
# делаем заглавными буквы всех слов
title_words_list = list(map(int_func, words_list))
# разделяем слова пробелами и ковертируем в предложение
new_sentence = "".join(list(map(lambda x: x + ' ', title_words_list))).strip()

print(new_sentence)
