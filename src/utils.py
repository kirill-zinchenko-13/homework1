import json
import logging
import os

# Создание папки logs, если она не существует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Создание отдельного логера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Установлен уровень логирования не ниже DEBUG

# Настройка file_handler для логера модуля utils
file_handler = logging.FileHandler("logs/utils.log")
file_handler.setLevel(logging.DEBUG)  # Установлен уровень логирования не ниже DEBUG

# Настройка форматтера для логера модуля utils
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)  # Установлен форматер для логера модуля utils

# Добавление handler к логеру модуля utils
logger.addHandler(file_handler)


def load_transactions_from_json(file_path):
    """Загружает данные о транзакциях из JSON-файла.

    Args:
        file_path (str): Путь до JSON-файла.

    Returns:
        list: Список словарей с данными о транзакциях или пустой список.
    """
    if not os.path.exists(file_path):
        logger.warning("Файл по пути '%s' не найден. Возвращаем пустой список.", file_path)
        return []

    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Успешно загружены %d транзакций из файла '%s'.", len(data), file_path)
                return data
            else:
                logger.warning("Данные в файле '%s' не являются списком. Возвращаем пустой список.", file_path)
                return []
        except json.JSONDecodeError as e:
            logger.error("Ошибка декодирования JSON в файле '%s': %s", file_path, e)
            return []
