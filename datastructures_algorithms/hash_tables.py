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
