# Список из нескольких строк для тестирования работы функции check_if_palindrome()
TESTS = ['Аргентина манит негра',
         'аргентина манит негра',
         'Манит Аргентина негра']


# Функция, которая проверяет, является ли переданная строка string палиндромом
def check_if_palindrome(string):
    # Для упрощения процесса проверки удаляем пробелы между словами
    # И переводим строку в нижний регистр
    prepared_str = string.replace(' ', '').lower()
    # Используем срез с обратным шагом, чтобы перевернуть строку задом наперед
    # Если строка равна своей перевернутой копии
    if prepared_str == prepared_str[::-1]:
        # Возвращаем логическое True
        return True
    else:
        # Возвращаем логическое False
        return False


if __name__ == 'main':
    # Прогоняем в цикле все тестовые строки из списка
    # Для каждой строки вызываем функцию, выполняем проверку и печатаем результат
    for item in TESTS:
        print('Строка является палиндромом:', check_if_palindrome(item))