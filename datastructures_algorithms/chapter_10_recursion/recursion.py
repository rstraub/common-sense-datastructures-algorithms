def print_every_other(low, high):
    # Base case
    if low > high:
        return

    print(low)
    print_every_other(low + 2, high)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 2)


def sum_numbers(low, high):
    if high > low:
        return high + sum_numbers(low, high - 1)
    else:
        return low


def recursive_flatten(data):
    result = []

    for value in data:
        if isinstance(value, list):
            result.extend(recursive_flatten(value))
        else:
            result.append(value)

    return result
