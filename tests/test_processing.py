import pytest

from datetime import datetime

from src.processing import filter_by_state, sort_by_date


# Пример данных для тестирования
@pytest.fixture
def transactions():
    return [
        {"id": 1, "date": datetime(2023, 1, 1), "state": "EXECUTED"},
        {"id": 2, "date": datetime(2023, 1, 2), "state": "PENDING"},
        {"id": 3, "date": datetime(2023, 1, 3), "state": "EXECUTED"},
        {"id": 4, "date": datetime(2023, 1, 4), "state": "CANCELLED"},
        {"id": 5, "date": datetime(2023, 1, 5), "state": "EXECUTED"},
        {"id": 6, "date": datetime(2023, 1, 5), "state": "PENDING"},  # одинаковая дата
    ]

def test_filter_by_state(transactions):
    # Параметризованные тесты для фильтрации по статусу
    states_to_test = [
        ("EXECUTED", [1, 3, 5]),
        ("PENDING", [2, 6]),
        ("CANCELLED", [4]),
        ("UNKNOWN", []),  # Нет таких статусов
    ]

    for state, expected_ids in states_to_test:
        filtered_transactions = filter_by_state(transactions, state=state)
        assert len(filtered_transactions) == len(expected_ids)
        assert all(tx["id"] in expected_ids for tx in filtered_transactions)

def test_sort_by_date(transactions):
    # Тестируем сортировку по дате (по умолчанию убывание)
    sorted_transactions_desc = sort_by_date(transactions)
    assert sorted_transactions_desc[0]["date"] == datetime(2023, 1, 5)
    assert sorted_transactions_desc[-1]["date"] == datetime(2023, 1, 1)

    # Тестируем сортировку по дате в порядке возрастания
    sorted_transactions_asc = sort_by_date(transactions, reverse=False)
    assert sorted_transactions_asc[0]["date"] == datetime(2023, 1, 1)
    assert sorted_transactions_asc[-1]["date"] == datetime(2023, 1, 5)

    # Проверка корректности сортировки при одинаковых датах
    sorted_transactions_same_date = [
        {"id": 7, "date": datetime(2023, 1, 5), "state": "EXECUTED"},
        {"id": 8, "date": datetime(2023, 1, 5), "state": "PENDING"},
    ]
    sorted_transactions = sort_by_date(sorted_transactions_same_date)
    assert sorted_transactions[0]["id"] == 7 or sorted_transactions[0]["id"] == 8
    assert sorted_transactions[1]["id"] != sorted_transactions[0]["id"]

    # Тестирование на некорректные форматы дат
    with pytest.raises(TypeError):
        sort_by_date(transactions + [{"id": 9, "date": "not-a-date", "state": "EXECUTED"}])
