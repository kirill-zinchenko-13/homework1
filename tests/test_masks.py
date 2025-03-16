import pytest

from src.masks import get_mask_card_number, get_mask_account

# Фикстура для тестовых данных


@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "1234 56 ** 3456"),
        ("9876543210987654", "9876 54 ** 7654"),
        ("1111222233334444", "1111 22 ** 4444"),
        ("5555666677778888", "5555 66 ** 8888"),
        ("0000111122223333", "0000 11 ** 3333"),
    ]


# Параметризованный тест
@pytest.mark.parametrize("input_card, expected_output", [
    ("1234567890123456", "1234 56 ** 3456"),
    ("9876543210987654", "9876 54 ** 7654"),
    ("1111222233334444", "1111 22 ** 4444"),
    ("5555666677778888", "5555 66 ** 8888"),
    ("0000111122223333", "0000 11 ** 3333"),
])
def test_get_mask_card_number(input_card, expected_output):
    assert get_mask_card_number(input_card) == expected_output


# Тест с использованием фикстуры
def test_get_mask_card_number_with_fixture(card_numbers):
    for card_number, expected in card_numbers:

        assert get_mask_card_number(card_number) == expected


# Фикстура для тестовых данных
@pytest.fixture
def account_numbers():
    return [
        ("123456789012", "**9012"),
        ("9876543210", "**3210"),
        ("1111222233334444", "**4444"),
        ("5555666677778888", "**8888"),

        ("000011112222", "**2222"),
    ]


# Параметризованный тест
@pytest.mark.parametrize("input_account, expected_output", [
    ("123456789012", "**9012"),
    ("9876543210", "**3210"),
    ("1111222233334444", "**4444"),
    ("5555666677778888", "**8888"),
    ("000011112222", "**2222"),

])
def test_get_mask_account(input_account, expected_output):

    assert get_mask_account(input_account) == expected_output

# Тест с использованием фикстуры


def test_get_mask_account_with_fixture(account_numbers):
    for account_number, expected in account_numbers:
        assert get_mask_account(account_number) == expected
