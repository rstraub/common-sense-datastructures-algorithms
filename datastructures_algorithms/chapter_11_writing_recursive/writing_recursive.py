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


def find_x(text):
    if text[0] == "x":
        return 0
    else:
        return find_x(text[1 : len(text)]) + 1


def unique_paths(rows, columns):
    if rows == 1 and columns == 1:
        return 0
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
