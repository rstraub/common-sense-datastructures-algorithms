import string


def intersection(array1, array2):
    result = []
    temp = {}

    for item in array1:
        temp[item] = True

    for item in array2:
        if item in temp:
            result.append(item)

    return result


def find_duplicate(chars):
    known_chars = {}

    for char in chars:
        if char in known_chars:
            return char
        else:
            known_chars[char] = True

    return None


def find_missing_letter(sentence):
    used_chars = {}
    for letter in sentence:
        unique_char = letter.lower()
        used_chars[unique_char] = True

    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in used_chars:
            return letter
    return None


def find_non_duplicate_letter(word):
    known_letters = {}

    # Tally the letters in the word: { 'a': 2, 'b': 3, ... }
    for letter in word:
        if letter in known_letters:
            known_letters[letter] = known_letters[letter] + 1
        else:
            known_letters[letter] = 1

    # Return first word with 1 occurrence
    for letter in word:
        if known_letters[letter] == 1:
            return letter

    return None
