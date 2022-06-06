def count_chars(texts):
    if not texts:
        return 0

    # Number of chars in current string
    return len(texts[0]) + count_chars(texts[1 : len(texts)])


def select_even(numbers):
    if not numbers:
        return []

    remainder = select_even(numbers[1 : len(numbers)])
    if numbers[0] % 2 == 0:
        result = [numbers[0]]
        result.extend(remainder)
        return result
    else:
        return remainder


def triangle(n):
    if n == 1:
        return 1

    return n + triangle(n - 1)
