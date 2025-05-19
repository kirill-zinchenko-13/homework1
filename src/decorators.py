from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования вызовов функций.

    Записывает в лог информацию о начале и завершении выполнения функции,
    а также об ошибках, если таковые возникают.

    Аргументы:
        filename: Имя файла для записи логов (если None, выводит в консоль).

    Возвращает:
        Обернутую функцию с логированием.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                log_start = f"Вызов функции '{func.__name__}' с аргументами: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(log_start + "\n")
                else:
                    print(log_start)

                result = func(*args, **kwargs)

                log_info = f"Функция '{func.__name__}' завершена успешно. Результат: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(log_info + "\n")
                else:
                    print(log_info)

                return result
            except Exception as e:
                log_error = f"Ошибка в функции '{func.__name__}': {type(e).__name__} с аргументами: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(log_error + "\n")
                else:
                    print(log_error)
                raise e

        return wrapper

    return decorator


# Пример использования декоратора


@log(filename="mylog.txt")
def add(a, b):
    """
    Возвращает сумму двух чисел.

    Аргументы:
        a (int, float): Первое число.
        b (int, float): Второе число.

    Возвращает:
        int, float: Сумма a и b.
    """
    return a + b


@log(filename="mylog.txt")
def divide(x, y):
    """
    Делит первое число на второе.

    Аргументы:
        x (int, float): Числитель.
        y (int, float): Знаменатель.

    Возвращает:
        float: Результат деления x на y.

    Исключения:
        ZeroDivisionError: Если y равно 0.
    """
    return x / y


# Примеры вызова функций
if __name__ == "__main__":
    print(add(5, 3))  # Ожидается 8
    print(divide(10, 2))  # Ожидается 5
    try:
        print(divide(10, 0))  # Ожидается ошибка деления на ноль
    except ZeroDivisionError:
        pass  # Игнорируем ошибку для примера
