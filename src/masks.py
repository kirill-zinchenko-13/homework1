def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return f"**{account_number[-4:]}"


print(get_mask_account(str(73654108430135874305)))
