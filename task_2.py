
print('\nЗадание №2 \n**** Функция вывода данных пользователя ****')


def print_personal_data(name, surname, year_of_birth, city, email, phone):
    """Выводит данные о пользоветеле одной строкой

    :param name: str
    :param surname: str
    :param year_of_birth: str
    :param city: str
    :param email: str
    :param phone: str
    :return: None
    """
    print(f'{name:15} | {surname:15} | {year_of_birth:10} | {city:15} | {email:20} | {phone:13}')


print_personal_data(surname='Иванов', name='Витя', city='Иваново',
                    phone='899112345678', email='ivanov2000@mail.ru', year_of_birth='2000')
