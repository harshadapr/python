def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
