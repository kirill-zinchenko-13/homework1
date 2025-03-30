def get_mask_card_number(card_number: str) -> str:
    # Убираем все пробелы для обработки
    clean_number = card_number.replace(" ", "")

    # Формируем маску для полных 16-значных номеров
    masked_parts = [
        clean_number[:4],  # первые 4 цифры показываем
        clean_number[4:6],  # следующие 2 цифры показываем
        "**",  # следующие 2 цифры маскируем
        "****",  # третьи 4 цифры маскируем
        clean_number[-4:]  # последние 4 цифры показываем
    ]

    # Возвращаем маску с правильными пробелами между группами
    return " ".join(masked_parts[:2]) + " ".join(masked_parts[2:])


def get_mask_account(account_number: str) -> str:
    # Получаем последние 4 цифры
    last_part = account_number[-4:]
    return f"**{last_part}"


def mask_card_number(card_info: str) -> str:
    """Вызываем необходимые функции"""
    if card_info.startswith("Счет"):
        return get_mask_account(card_info)
    else:
        return get_mask_card_number(card_info)
