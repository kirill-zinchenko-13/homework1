def filter_by_currency(transactions, currency_code):
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


# Пример использования:
if __name__ == "__main__":
    # Пример списка транзакций
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

    # Получаем итератор для транзакций в USD
    usd_transactions = filter_by_currency(transactions, "USD")

    # Выводим все USD транзакции
    print("Все USD транзакции:")
    for transaction in usd_transactions:
        print(transaction)

    # Пример получения транзакций по одной
    print("\nПолучение транзакций по одной:")
    try:
        print(next(usd_transactions))  # Первая USD транзакция
        print(next(usd_transactions))  # Вторая USD транзакция
    except StopIteration:
        print("Больше транзакций в данной валюте нет")


def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описания транзакций

    :param transactions: список словарей с транзакциями
    :return: генератор описаний транзакций
    """
    for transaction in transactions:
        # Получаем описание транзакции, используя безопасный доступ к вложенным словарям
        description = transaction.get("description", "Описание отсутствует")
        yield description


# Пример использования:
if __name__ == "__main__":
    # Пример списка транзакций
    transactions = [
        {
            "id": 1,
            "description": "Оплата услуг мобильной связи",
            "amount": 500
        },
        {
            "id": 2,
            "description": "Перевод другу",
            "amount": 1000
        },
        {
            "id": 3,
            "amount": 2000
        },
        {
            "id": 4,
            "description": "Покупка в магазине",
            "amount": 1500
        }
    ]

    # Получаем генератор описаний
    descriptions = transaction_descriptions(transactions)

    # Выводим все описания
    for description in descriptions:
        print(description)

    # Пример получения описаний по одному
    print("\nПолучение описаний по одному:")
    try:
        print(next(descriptions))  # Оплата услуг мобильной связи
        print(next(descriptions))  # Перевод другу
        print(next(descriptions))  # Описание отсутствует
        print(next(descriptions))  # Покупка в магазине
    except StopIteration:
        print("Больше описаний нет")


def card_number_generator(start: str, stop: str):
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
        yield " ".join(card_number[i:i + 4] for i in range(0, 16, 4))


def is_valid_card_number(number: str):
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

# Пример использования:
# for card in card_number_generator("0000 0000 0000 0001", "0000 0000 0000 0010"):
#     print(card)
