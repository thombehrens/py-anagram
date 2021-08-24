import requests
import collections
import time

start = time.time()

# Get words
def get_words():
    url = "https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt"
    webpage = requests.get(url)
    word_blob = webpage.text
    words = word_blob.split()
    return words


# Get 1 word anagrams
def get_valid_words(words, letters):
    valid_words = words.copy()
    for word in words:
        allowed_letters = letters.copy()
        for word_letter in word:
            if word_letter in allowed_letters:
                allowed_letters.remove(word_letter)
                continue
            else:
                valid_words.remove(word)
                break
    return valid_words


# Get two word anagrams
def get_valid_pairs(valid_words, letters):
    valid_pairs = []
    for index, word in enumerate(valid_words):
        first_word_letters = list(word)
        i = index + 1
        while i < len(valid_words):
            pair = first_word_letters + list(valid_words[i])
            if collections.Counter(pair) == collections.Counter(letters):
                valid_pairs.append(word + ", " + valid_words[i])
                i += 1
    return valid_pairs


letters = list("DOCUMENTING")
words = get_words()
valid_words = get_valid_words(words, letters)
valid_pairs = get_valid_pairs(valid_words, letters)
print(valid_pairs)

end = time.time()

print("Execution time: ", end - start, "seconds")
