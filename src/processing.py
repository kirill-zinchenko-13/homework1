def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями.
    :param state: Значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующий указанному значению 'state'.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция сортирует список словарей по значению ключа 'date'.

    :param transactions: Список словарей с транзакциями.
    :param reverse: Параметр, указывающий порядок сортировки (по умолчанию True - убывание).
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(
        transactions,
        key=lambda x: (x.get("date") is None, x.get("date")),  # Сначала сортируем по наличию даты
        reverse=reverse
    )