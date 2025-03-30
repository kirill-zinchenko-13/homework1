import pytest

from src.widget import mask_card_number, get_data


# Фикстура для тестовых данных


@pytest.fixture
def test_data():
    return [
        ("Счет 123456789012", "**9012"),  # Тест для счета
        ("Счет 9876543210", "**3210"),  # Тест для счета
        ("1234 5678 9012 3456", "1234 56** **** 3456"),  # Тест для карты
        ("9876 5432 1098 7654", "9876 54** **** 7654"),  # Тест для карты
    ]


# Параметризованный тест
@pytest.mark.parametrize("input_card_info, expected_output", [
    ("Счет 123456789012", "**9012"),
    ("Счет 9876543210", "**3210"),
    ("1234 5678 9012 3456", "1234 56** **** 3456"),
    ("9876 5432 1098 7654", "9876 54** **** 7654"),
])
def test_mask_card_number(input_card_info, expected_output):
    assert mask_card_number(input_card_info) == expected_output


# Тест с использованием фикстуры
def test_mask_card_number_with_fixture(test_data):
    for card_info, expected in test_data:
        assert mask_card_number(card_info) == expected


# Фикстура для тестовых данных
@pytest.fixture
def test_data_new():
    return [
        ("2023-10-01T12:30:45.123456", "01.10.2023"),  # Тест с полной датой и временем
        ("2022-05-15T08:00:00.000000", "15.05.2022"),  # Тест с другой датой
        ("2000-01-01T00:00:00.000000", "01.01.2000"),  # Граничный случай
        ("1999-12-31T23:59:59.999999", "31.12.1999"),  # Граничный случай

    ]


# Параметризованный тест
@pytest.mark.parametrize("input_date_str, expected_output", [
    ("2023-10-01T12:30:45.123456", "01.10.2023"),
    ("2022-05-15T08:00:00.000000", "15.05.2022"),
    ("2000-01-01T00:00:00.000000", "01.01.2000"),
    ("1999-12-31T23:59:59.999999", "31.12.1999"),
])
def test_get_data(input_date_str, expected_output):
    assert get_data(input_date_str) == expected_output


# Тест с использованием фикстуры


def test_get_data():
    # Тестовые данные: (входная строка, ожидаемый результат)
    test_cases = [
        ("2025-03-30T12:34:56.789", "30.03.2025"),
        ("2024-01-01T00:00:00.000", "01.01.2024"),
        ("1999-12-31T23:59:59.999", "31.12.1999"),
        ("2000-02-29T12:00:00.000", "29.02.2000"),  # високосный год
        ("2025-03-30T23:59:59.999", "30.03.2025"),
    ]

    for input_date, expected_output in test_cases:
        assert get_data(input_date) == expected_output


def test_get_data_invalid_input():
    # Проверяем обработку некорректных данных
    with pytest.raises(ValueError):
        get_data("некорректная строка")

    with pytest.raises(ValueError):
        get_data("2025-30-30T12:34:56.789")
