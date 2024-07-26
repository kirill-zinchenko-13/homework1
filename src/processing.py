def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями.
    :param state: Значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующий указанному значению 'state'.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]
