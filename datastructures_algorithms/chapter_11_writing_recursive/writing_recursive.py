def count_chars(texts):
    if not texts:
        return 0

    # Number of chars in current string
    return len(texts[0]) + count_chars(texts[1 : len(texts)])
