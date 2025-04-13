import functools
import logging

def log(filename='mylog_decorators.txt'):
    # Настраиваем логирование
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Начало выполнения функции '{func.__name__}' с аргументами: {args}, {kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.info(f"Функция '{func.__name__}' завершена успешно. Результат: {result}")
                return result
            except Exception as e:
                logging.error(f"Ошибка при выполнении функции '{func.__name__}': {e}")
                raise  # Повторно выбрасываем исключение после логирования

        return wrapper

    return decorator

# Пример использования декоратора
@log('mylog_decorators.txt')
def divide(a, b):
    return a / b

if __name__ == "__main__":
    try:
        print(divide(10, 2))
        print(divide(10, 0))  # Это вызовет ошибку деления на ноль
    except ZeroDivisionError:
        pass
