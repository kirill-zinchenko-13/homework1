import logging
import functools

# Настройка логирования для вывода в консоль
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log(func):
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
    return a + b


@log
def divide(x, y):
    return x / y

# Примеры вызова функций


if __name__ == "__main__":
    print(add(5, 3))  # Ожидается 8
    print(divide(10, 2))  # Ожидается 5
    try:
        print(divide(10, 0))  # Ожидается ошибка деления на ноль
    except ZeroDivisionError:
        pass  # Игнорируем ошибку для примера
