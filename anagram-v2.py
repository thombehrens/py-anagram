import requests
from collections import Counter
import time

start = time.time()


def get_words():
    url = "https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt"
    return requests.get(url).text.split()


def get_bad_words():
    url = "https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt"
    return requests.get(url).text.split()


def get_valid_words(all_words, bad_words, anagram_word):
    valid_words = all_words.copy()
    for word in all_words:
        if len(Counter(word) - Counter(anagram_word)) > 0:
            valid_words.remove(word)
        elif word in bad_words:
            valid_words.remove(word)
    return valid_words


def print_valid_pairs(valid_words, anagram_word):
    for index, first_word in enumerate(valid_words):
        i = index + 1
        while i < len(valid_words):
            second_word = valid_words[i]
            if Counter(first_word + second_word) == Counter(anagram_word):
                print(anagram_word, " = ", first_word, " + ", second_word)
            i += 1


# TODO: Case insensitivity

anagram_word = "DOCUMENTING"
all_words = get_words()
bad_words = get_bad_words()
valid_words = get_valid_words(all_words, bad_words, anagram_word)
print_valid_pairs(valid_words, anagram_word)

end = time.time()

print("Execution time: ", end - start, "seconds")
