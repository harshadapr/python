def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

input_sentence = "The quick brown fox jumps over the lazy dog"
longest_word = find_longest_word(input_sentence)
print(f"The longest word in the sentence is: {longest_word}")
