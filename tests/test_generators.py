import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def valid_card_numbers():
    return [
        "0000 0000 0000 0001",
        "1234 5678 9012 3456",
        "9999 9999 9999 9999"
    ]


@pytest.mark.parametrize("start,end,expected_count", [
    ("0000 0000 0000 0001", "0000 0000 0000 0010", 10),
    ("1111 1111 1111 1111", "1111 1111 1111 1120", 10),
    ("9999 9999 9999 9980", "9999 9999 9999 9999", 20)
])
def test_card_generator_range(start, end, expected_count):
    generated_numbers = list(card_number_generator(start, end))
    assert len(generated_numbers) == expected_count
    assert generated_numbers[0] == start
    assert generated_numbers[-1] == end


def test_card_generator_format(valid_card_numbers):
    for number in valid_card_numbers:
        generated_numbers = list(card_number_generator(number, number))
        assert len(generated_numbers) == 1
        assert generated_numbers[0] == number
        assert len(generated_numbers[0].split(" ")) == 4
        assert all(part.isdigit() for part in generated_numbers[0].split(" "))


@pytest.mark.parametrize("start,end", [
    ("0000 0000 0000 0001", "0000 0000 0000 0001"),
    ("9999 9999 9999 9999", "9999 9999 9999 9999")
])
def test_card_generator_single_value(start, end):
    generated_numbers = list(card_number_generator(start, end))
    assert len(generated_numbers) == 1
    assert generated_numbers[0] == start


@pytest.mark.parametrize("invalid_input", [
    "1234567890123456",  # Нет пробелов
    "1234 5678 9012 345",  # Недостаточно цифр
    "1234 5678 9012 34567",  # Слишком много цифр
    "abcd abcd abcd abcd",  # Буквы вместо цифр
    "1234 5678 9012",  # Неправильный формат
    "1234 5678 9012 3456 7890",  # Слишком много групп
])
def test_card_generator_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        list(card_number_generator(invalid_input, invalid_input))


@pytest.mark.parametrize("start,end", [
    ("0000 0000 0000 0002", "0000 0000 0000 0001"),
    ("9999 9999 9999 9999", "0000 0000 0000 0001"),
    ("1234 5678 9012 3456", "1234 5678 9012 3455")
])
def test_card_generator_invalid_range(start, end):
    with pytest.raises(ValueError):
        list(card_number_generator(start, end))


# Тестирование получения описаний транзакций
def test_transaction_descriptions():
    transactions = [
        {
            "id": 1,
            "description": "Оплата услуг",
            "amount": 500
        },
        {
            "id": 2,
            "amount": 1000
        },
        {
            "id": 3,
            "description": "Перевод",
            "amount": 2000
        }
    ]

    expected = [
        "Оплата услуг",
        "Описание отсутствует",
        "Перевод"
    ]

    assert list(transaction_descriptions(transactions)) == expected


# Тестирование фильтрации по валюте
def test_filter_by_currency_usd():
    transactions = [
        {
            "id": 1,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Оплата услуг"
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {
                    "code": "RUB"
                }
            },
            "description": "Перевод другу"
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Покупка в магазине"
        },
        {
            "id": 4,
            "description": "Перевод",
            "operationAmount": {}
        }
    ]

    # Проверка фильтрации по USD
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["description"] == "Оплата услуг"
    assert usd_transactions[1]["description"] == "Покупка в магазине"


def test_filter_by_currency_empty():
    transactions = [
        {
            "id": 1,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Оплата услуг"
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {
                    "code": "RUB"
                }
            },
            "description": "Перевод другу"
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            },
            "description": "Покупка в магазине"
        },
        {
            "id": 4,
            "description": "Перевод",
            "operationAmount": {}
        }
    ]

    # Проверка отсутствия транзакций по несуществующей валюте
    empty_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(empty_transactions) == 0


# Тестирование граничных случаев filter_by_currency
def test_filter_by_currency_empty_transactions():
    empty_list = []
    result = list(filter_by_currency(empty_list, "USD"))
    assert len(result) == 0


def test_filter_by_currency_missing_fields():
    transactions = [
        {
            "id": 1,
            "description": "Оплата услуг"
        },
        {
            "id": 2,
            "operationAmount": {}
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {}
            }
        }
    ]

    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 0
