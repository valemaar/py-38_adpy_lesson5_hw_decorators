# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
# 3. Применить написанный логгер к приложению из любого предыдущего д/з.


from datetime import datetime


# task 1


def logger(function):
    def function_replaced(*args, **kwargs):
        current_date_string = datetime.today().strftime('%m/%d/%y %H:%M:%S')
        result = function(*args, **kwargs)
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(f'Дата вызова функции: {current_date_string}, Имя функции: {function.__name__},'
                    f' аргументы: {[*args, *kwargs]}, Результат вызова: {result}.')
        return result

    return function_replaced


@logger
def old_function(a, b):
    c = a + b
    print('Вызвана функция old_function')
    return c


old_function(2, 3)


# task 2

def logger(log_file):
    def _logger(function):
        def function_replaced(*args, **kwargs):
            current_date_string = datetime.today().strftime('%m/%d/%y %H:%M:%S')
            result = function(*args, **kwargs)
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(f'Дата вызова функции: {current_date_string}; Имя функции: {function.__name__};'
                        f' Аргументы: {[*args, *kwargs]}; Результат вызова: {result}.')
            return result

        return function_replaced

    return _logger


@logger(r'c:\new_folder\new_log.txt')
def old_function(a, b):
    c = a + b
    print('Вызвана функция old_function')
    return c


old_function(5, 6)
