def print_every_other(low, high):
    # Base case
    if low > high:
        return

    print(low)
    print_every_other(low + 2, high)


class TestRecurse:
    def test_print_every_other(self):
        print_every_other(0, 10)
