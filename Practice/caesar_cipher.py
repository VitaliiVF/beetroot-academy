from string import punctuation 

def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    letter = letter.lower()    
    new_letter = chr(((ord(letter) + shift - 97) % 26) + 97)
    return new_letter

def caesar_cipher(letters: str, shift: int) -> str:
    """Функция реализовывает шифр Цезаря"""
    cipher = ""
    for i in letters:
        if i in punctuation or i == " ":
            cipher += i
        else:
            cipher += shift_letter(i, shift)
    return cipher

print(caesar_cipher('leave out all !!!t., rest', -1))