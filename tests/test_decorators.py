import os

import pytest

from src.decorators import add, divide

# Убедитесь, что файл лога не существует перед тестами
log_file = "mylog.txt"


@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Удаляет файл лога перед и после тестов."""
    if os.path.exists(log_file):
        os.remove(log_file)
    yield
    if os.path.exists(log_file):
        os.remove(log_file)


def test_add():
    """Тест для функции сложения."""
    result = add(5, 3)
    assert result == 8

    # Проверка содержимого файла лога
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
    assert "Функция 'add' завершена успешно. Результат: 8" in log_content


def test_divide():
    """Тест для функции деления."""
    result = divide(10, 2)
    assert result == 5

    # Проверка содержимого файла лога
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
    assert "Функция 'divide' завершена успешно. Результат: 5" in log_content


def test_divide_by_zero():
    """Тест для деления на ноль, ожидается ошибка."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # Проверка содержимого файла лога на наличие ошибки
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
    assert "Ошибка в функции 'divide': ZeroDivisionError" in log_content
