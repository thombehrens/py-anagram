import sys
import time
import requests
from collections import Counter
from os.path import exists

start = time.time()


def get_words(filename, url):
    if exists(filename):
        file = open(filename, "r")
        words = file.read().split()
    else:
        text = requests.get(url).text
        file = open(filename, "w")
        file.write(text)
        words = text.split()
    file.close()
    return words


def get_all_words():
    return get_words(
        "all_words.txt",
        "https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt",
    )


def get_bad_words():
    return get_words(
        "bad_words.txt",
        "https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt",
    )


def find_valid_words(all_words, bad_words, anagram_word):
    valid_words = all_words.copy()
    for word in all_words:
        if len(Counter(word.lower()) - Counter(anagram_word)) > 0:
            valid_words.remove(word)
        elif word.lower() in bad_words:
            valid_words.remove(word)
    return valid_words


def find_valid_pairs(valid_words, anagram_word):
    valid_pairs = []
    for index, word in enumerate(valid_words):
        first_word = word.lower()
        i = index + 1
        while i < len(valid_words):
            second_word = valid_words[i].lower()
            if Counter(first_word + second_word) == Counter(anagram_word):
                valid_pairs.append((first_word, second_word))
            i += 1
    return valid_pairs


def print_valid_pairs(valid_pairs, anagram_word):
    for pair in valid_pairs:
        print(anagram_word, " = ", pair[0], " + ", pair[1])


if len(sys.argv) == 1:
    anagram_word = "documenting"
elif len(sys.argv) == 2:
    anagram_word = sys.argv[1]
else:
    print("usage: anagram-v3.py <anagram_word>")
    exit
all_words = get_all_words()
bad_words = get_bad_words()
valid_words = find_valid_words(all_words, bad_words, anagram_word)
valid_pairs = find_valid_pairs(valid_words, anagram_word)
print_valid_pairs(valid_pairs, anagram_word)

end = time.time()

print("Execution time: ", end - start, "seconds")
