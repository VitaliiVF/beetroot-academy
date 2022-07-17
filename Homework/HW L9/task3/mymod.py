def count_lines(name):
    return len(name.readlines())

def count_chars(name):
    count = 0
    for lines in name.read():
        count += len(lines)
    return count

def test():
    file = input("Enter file name: ")
    name = open(file)
    
    lines = count_lines(name)
    name.seek(0)
    chars = count_chars(name)
    
    return f"""Number of lines in the file: {lines}
Number of characters in the file: {chars}"""

print(test())