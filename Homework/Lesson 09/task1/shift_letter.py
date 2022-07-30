def shift_letter(letter: str, shift: int) -> str:
    """Функція зсуває символ letter на shift позицій

    Args:
        letter (str): символ, який потрібно замінити
        shift (int): зсув символу

    Returns:
        str: новий символ після зсуву letter по алфавіту
    """
    letter = letter.lower()    
    new_letter = chr(((ord(letter) + shift - 97) % 26) + 97)
    return new_letter