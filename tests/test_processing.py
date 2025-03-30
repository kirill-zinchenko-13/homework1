import pytest

from datetime import datetime

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions_data():
    return [
        {"id": 1, "amount": 100, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 2, "amount": 200, "date": "2023-09-15", "state": "PENDING"},
        {"id": 3, "amount": 300, "date": "2023-10-05", "state": "EXECUTED"},
        {"id": 4, "amount": 400, "date": "2023-08-20", "state": "CANCELLED"},
        {"id": 5, "amount": 500, "date": "2023-09-30", "state": "EXECUTED"},
    ]


# Параметризованный тест
@pytest.mark.parametrize("input_state, expected_output", [
    ("EXECUTED", [
        {"id": 1, "amount": 100, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 3, "amount": 300, "date": "2023-10-05", "state": "EXECUTED"},
        {"id": 5, "amount": 500, "date": "2023-09-30", "state": "EXECUTED"},
    ]),
    ("PENDING", [
        {"id": 2, "amount": 200, "date": "2023-09-15", "state": "PENDING"},
    ]),
    ("CANCELLED", [
        {"id": 4, "amount": 400, "date": "2023-08-20", "state": "CANCELLED"},
    ]),
    ("UNKNOWN", []),  # Состояние не найдено
])
def test_filter_by_state(transactions_data, input_state, expected_output):
    assert filter_by_state(transactions_data, input_state) == expected_output


# Тест с использованием фикстуры для фильтрации по умолчанию
def test_filter_by_state_default(transactions_data):
    expected_output = [
        {"id": 1, "amount": 100, "date": "2023-10-01", "state": "EXECUTED"},
        {"id": 3, "amount": 300, "date": "2023-10-05", "state": "EXECUTED"},
        {"id": 5, "amount": 500, "date": "2023-09-30", "state": "EXECUTED"},
    ]
    assert filter_by_state(transactions_data, 'EXECUTED') == expected_output


@pytest.fixture
def transactions_data_new():
    return [
        {"id": 1, "amount": 100, "date": datetime(2023, 10, 1)},
        {"id": 2, "amount": 200, "date": datetime(2023, 9, 15)},
        {"id": 3, "amount": 300, "date": datetime(2023, 10, 5)},  # Эта транзакция должна быть здесь
        {"id": 4, "amount": 400, "date": datetime(2023, 8, 20)},
        {"id": 5, "amount": 500, "date": datetime(2023, 9, 30)},
    ]


# Тест с использованием фикстуры для сортировки по умолчанию (убывание)
def test_sort_by_date_default(transactions_data_new):
    expected_order = [
        {"id": 3, "amount": 300, "date": datetime(2023, 10, 5)},
        {"id": 1, "amount": 100, "date": datetime(2023, 10, 1)},
        {"id": 5, "amount": 500, "date": datetime(2023, 9, 30)},
        {"id": 2, "amount": 200, "date": datetime(2023, 9, 15)},
        {"id": 4, "amount": 400, "date": datetime(2023, 8, 20)},
    ]
    assert sort_by_date(transactions_data_new) == expected_order
