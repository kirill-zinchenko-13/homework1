import logging
import os

# Создание папки logs, если она не существует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Создание отдельного логера для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Установлен уровень логирования не ниже DEBUG

# Настройка file_handler для логера модуля masks
file_handler = logging.FileHandler("logs/masks.log")
file_handler.setLevel(logging.DEBUG)  # Установлен уровень логирования не ниже DEBUG

# Настройка форматтера для логера модуля masks
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)  # Установлен форматер для логера модуля masks

# Добавление handler к логеру модуля masks
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер кредитной карты."""
    logger.debug("Получен номер карты для маскировки: %s", card_number)

    # Убираем все пробелы для обработки
    clean_number = card_number.replace(" ", "")

    # Формируем маску для полных 16-значных номеров
    masked_parts = [
        clean_number[:4],  # первые 4 цифры показываем
        clean_number[4:6],  # следующие 2 цифры показываем
        "**",  # следующие 2 цифры маскируем
        "****",  # третьи 4 цифры маскируем
        clean_number[-4:],  # последние 4 цифры показываем
    ]

    masked_number = " ".join(masked_parts[:2]) + " ".join(masked_parts[2:])
    logger.info("Сгенерирован замаскированный номер карты: %s", masked_number)

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    logger.debug("Получен номер счета для маскировки: %s", account_number)

    # Получаем последние 4 цифры
    last_part = account_number[-4:]
    masked_account = f"**{last_part}"

    logger.info("Сгенерирован замаскированный номер счета: %s", masked_account)

    return masked_account


def mask_card_number(card_info: str) -> str:
    """Вызывает необходимые функции для маскировки номера карты или счета."""
    logger.debug("Получена информация для маскировки: %s", card_info)

    try:
        if card_info.startswith("Счет"):
            return get_mask_account(card_info)
        else:
            return get_mask_card_number(card_info)
    except Exception as e:
        logger.error("Ошибка при маскировке номера: %s", e)
        return card_info  # Возвращаем оригинальную информацию в случае ошибки
