from string import ascii_lowercase

def is_pangram(text):
    text = text.lower()
    only_letter = ""
    
    for letter in text:
        if letter.isalpha():
            only_letter += letter

    for letter in ascii_lowercase:
        if letter in only_letter:
            result = True
        else:
            result = False
            break

    return result


def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    return False