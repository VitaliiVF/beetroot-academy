from shift_letter import shift_letter
from string import punctuation

def caesar_cipher(text: str, shift: int) -> str:
    """Функція здійснює шифр Цезаря

    Args:
        text (str): текст, який потрбіно зашифрувати
        shift (int): зсув, на який потрібно здійснити шифр

    Returns:
        str: зашифрований текст
    """
    cipher = ""
    for letter in text:
        if letter not in punctuation and letter != " ":
            cipher += shift_letter(letter, shift)
        else:
            cipher += letter
    return cipher

print(caesar_cipher('leave out all !!!t., rest', -1))