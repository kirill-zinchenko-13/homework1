from typing import Dict, Generator, List, Union


def filter_by_currency(
    transactions: List[Dict[str, Union[str, Dict]]], currency_code: str
) -> Generator[Dict[str, Union[str, Dict]], None, None]:
    """
    Генератор, фильтрующий транзакции по коду валюты

    :param transactions: список словарей с транзакциями
    :param currency_code: код валюты для фильтрации
    :return: генератор отфильтрованных транзакций
    """
    for transaction in transactions:
        # Получаем код валюты из вложенных словарей
        transaction_currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if transaction_currency == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Union[str, Dict]]]) -> Generator[str, None, None]:
    """
    Генератор, возвращающий описания транзакций

    :param transactions: список словарей с транзакциями
    :return: генератор описаний транзакций
    """
    for transaction in transactions:
        # Получаем описание транзакции, используя безопасный доступ к вложенным словарям
        description = transaction.get("description", "Описание отсутствует")
        yield description


def card_number_generator(start: str, stop: str) -> Generator[str, None, None]:
    # Проверка корректности входных данных
    if not is_valid_card_number(start):
        raise ValueError("Некорректный формат начального номера карты")

    if not is_valid_card_number(stop):
        raise ValueError("Некорректный формат конечного номера карты")

    if start > stop:
        raise ValueError("Начальное значение должно быть меньше конечного")

    # Преобразуем номера карт в числа для удобства работы
    start_num = int(start.replace(" ", ""))
    stop_num = int(stop.replace(" ", ""))

    # Генерируем номера карт в заданном диапазоне
    for num in range(start_num, stop_num + 1):
        # Форматируем номер карты
        card_number = "{:016d}".format(num)
        yield " ".join(card_number[i: i + 4] for i in range(0, 16, 4))


def is_valid_card_number(number: str) -> bool:
    # Проверяем формат номера карты
    if len(number) != 19:
        return False

    parts = number.split(" ")
    if len(parts) != 4:
        return False

    if not all(part.isdigit() for part in parts):
        return False

    if not all(len(part) == 4 for part in parts):
        return False

    # Проверяем, что номер находится в допустимом диапазоне
    number_without_spaces = number.replace(" ", "")
    if not (1 <= int(number_without_spaces) <= 9999999999999999):
        return False

    return True


if __name__ == "__main__":
    # Пример списка транзакций
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Оплата услуг"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод другу"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Покупка в магазине"},
        {"id": 4, "description": "Перевод", "operationAmount": {}},
    ]

    # Выводим все USD транзакции
    print("Все USD транзакции:")
    for transaction in filter_by_currency(transactions, "USD"):
        print(transaction)

    # Пример получения транзакций по одной
    print("\nПолучение транзакций по одной:")
    try:
        usd_transactions = filter_by_currency(transactions, "USD")
        for transaction in usd_transactions:
            print(transaction)
    except Exception as e:
        print(f"Произошла ошибка при обработке транзакций: {e}")
    finally:
        print("\nЗавершение обработки транзакций")
