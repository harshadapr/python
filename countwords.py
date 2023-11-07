def count_words(text):
    words = text.split()
    return len(words)

text = "This is a sample sentence."
word_count = count_words(text)
print(f"There are {word_count} words in the text.")
