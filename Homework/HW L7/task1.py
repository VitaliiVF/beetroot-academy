sentence = input().split()

unique_words = {word : sentence.count(word) for word in sentence}

print("All unique words in a sentence with the number of occurrences: ")

for key, value in unique_words.items():
    print(f"{key}: {value}")
