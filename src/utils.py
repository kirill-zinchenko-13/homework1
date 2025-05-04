import json
import os


def load_transactions_from_json(file_path):
    """Загружает данные о транзакциях из JSON-файла.

    Args:
        file_path (str): Путь до JSON-файла.

    Returns:
        list: Список словарей с данными о транзакциях или пустой список.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []
