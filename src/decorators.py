import functools
import logging

# Настройка логирования для записи в файл
logging.basicConfig(filename="mylog.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def log(func):
    """
    Декоратор для логирования вызовов функций.

    Записывает в лог информацию о начале и завершении выполнения функции,
    а также об ошибках, если таковые возникают.

    Аргументы:
        func: Функция, которую нужно обернуть.

    Возвращает:
        Обернутую функцию с логированием.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Логируем начало выполнения функции
        logging.info(f"Начало выполнения функции '{func.__name__}' с аргументами: {args}, {kwargs}")
        try:
            # Выполняем функцию
            result = func(*args, **kwargs)
            # Логируем успешное завершение
            logging.info(f"Функция '{func.__name__}' завершена успешно. Результат: {result}")
            return result
        except Exception as e:
            # Логируем ошибку
            logging.error(f"Ошибка в функции '{func.__name__}': {type(e).__name__} с аргументами: {args}, {kwargs}")
            raise  # Повторно выбрасываем исключение после логирования

    return wrapper


# Пример использования декоратора


@log
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


@log
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
