
text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

sorted_words = sorted(word_to_count.keys())

max_length = max((len(word) for word in sorted_words))
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")