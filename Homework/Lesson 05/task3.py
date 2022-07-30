from random import sample

word = input("Insert your string: ")
k = 1

while k <= 5:
    word = sample(word, len(word))
    word = "".join(word)
    print(f"New word №{k} – {word}")
    k += 1