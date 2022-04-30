def print_every_other(low, high):
    # Base case
    if low > high:
        return

    print(low)
    print_every_other(low + 2, high)


# stack overflows -> hits 0 and misses the base case of 1
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


class TestRecurse:
    def test_print_every_other(self):
        print_every_other(0, 10)

    def test_sum_should_sum_all_numbers_in_range(self):
        assert sum_numbers(0, 10) == 55
