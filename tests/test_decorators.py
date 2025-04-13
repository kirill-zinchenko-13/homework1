import pytest
import logging
from src.decorators import add, divide


def test_add(caplog):
    with caplog.at_level(logging.INFO):
        result = add(5, 3)

    # Проверяем результат функции
    assert result == 8

    # Проверяем логи
    assert "Начало выполнения функции 'add' с аргументами: (5, 3), {}" in caplog.text
    assert "Функция 'add' завершена успешно. Результат: 8" in caplog.text


def test_divide(caplog):
    with caplog.at_level(logging.INFO):
        result = divide(10, 2)

    # Проверяем результат функции
    assert result == 5

    # Проверяем логи
    assert "Начало выполнения функции 'divide' с аргументами: (10, 2), {}" in caplog.text
    assert "Функция 'divide' завершена успешно. Результат: 5" in caplog.text


def test_divide_by_zero(caplog):
    with pytest.raises(ZeroDivisionError):
        with caplog.at_level(logging.INFO):
            divide(10, 0)

    # Проверяем логи на наличие ошибки
    assert "Ошибка в функции 'divide': ZeroDivisionError с аргументами: (10, 0), {}" in caplog.text
