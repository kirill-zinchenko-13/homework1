import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_ACCESS_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data"


def get_exchange_rate(currency):
    """Получает текущий курс валюты к рублю.

    Args:
        currency (str): Код валюты (например, 'USD', 'EUR').

    Returns:
        float: Курс валюты к рублю или None в случае ошибки.
    """
    url = f"{BASE_URL}/latest?base={currency}&symbols=RUB"
    headers = {"apikey": API_ACCESS_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()

        if "rates" in data and "RUB" in data["rates"]:
            return data["rates"]["RUB"]
        else:
            return None
    except Exception as e:
        print(f"Ошибка при получении курса валюты: {e}")
        return None


def convert_to_rub(transaction):
    """Конвертирует сумму транзакции в рубли.

    Args:
        transaction (dict): Словарь с данными о транзакции, должен содержать ключи 'amount' и 'currency'.

    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return float(amount)

    exchange_rate = get_exchange_rate(currency)

    if exchange_rate is not None:
        return float(amount) * exchange_rate
    else:
        print(f"Не удалось получить курс для {currency}.")
        return 0.0
