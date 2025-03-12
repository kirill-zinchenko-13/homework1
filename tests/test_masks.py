import pytest

from src.widget import mask_card_number


# Фикстура для тестов карт
@pytest.fixture
def card_tests():
    return [
        ("1234567812345678", "1234 56 ** 5678"),
        ("4111111111111111", "4111 11 ** 1111"),
        ("5500000000000004", "5500 00 ** 0004"),  # Пробелы в номере карты
        ("4012888888881881", "4012 88 ** 1881"),
    ]

# Фикстура для тестов счетов
@pytest.fixture
def account_tests():
    return [
        ("Счет 123456789012", "**9012"),
        ("Счет 9876543210", "**3210"),
        ("Счет 100200300400", "**0400"),
        ("Счет 12345678", "**5678"),  # Счет с 8 цифрами
    ]

# Фикстура для некорректных входных данных
@pytest.fixture
def invalid_inputs():
    return [
        "Некорректный ввод",
        "Счет abcdefghij",
        "1234-5678-9012-3456",  # Неправильный формат номера карты
        "",  # Пустая строка
    ]

# Тесты для функции mask_card_number
def test_mask_card_number(card_tests, account_tests, invalid_inputs):
    # Тестирование карт
    for card_info, expected in card_tests:
        assert mask_card_number(card_info) == expected, f"Ошибка для карты: {card_info}"

    # Тестирование счетов
    for account_info, expected in account_tests:
        assert mask_card_number(account_info) == expected, f"Ошибка для счета: {account_info}"

    # Тесты на некорректный ввод
    for invalid_input in invalid_inputs:
        with pytest.raises((ValueError, TypeError)):
            mask_card_number(invalid_input)