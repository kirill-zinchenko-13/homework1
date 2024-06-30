
from masks import get_mask_card_number, get_mask_account


def mask_card_number(card_info: str) -> str:
    """Вызываем необходимые функции"""
    if card_info.startswith("Счет"):
        return get_mask_account(card_info)
    else:
        return get_mask_card_number(card_info)


from datetime import datetime


def get_data(date_str: str) -> str:
    """Преобразуем строку в объект datetime"""
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')

    # Форматируем дату в нужный вид
    formatted_date = date_obj.strftime('%d.%m.%Y')

    return formatted_date