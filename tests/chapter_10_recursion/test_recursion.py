from datastructures_algorithms.chapter_10_recursion.recursion import (
    print_every_other,
    recursive_flatten,
    sum_numbers,
)


class TestRecurse:
    def test_print_every_other(self):
        print_every_other(0, 10)

    def test_sum_should_sum_all_numbers_in_range(self):
        assert sum_numbers(0, 10) == 55

    def test_recursive_print(self):
        data = [
            1,
            2,
            3,
            [4, 5, 6],
            7,
            [8, [9, 10, 11, [12, 13, 14]]],
            [
                15,
                16,
                17,
                18,
                19,
                [20, 21, 22, [23, 24, 25, [26, 27, 28, 29]], 30, 31],
                32,
            ],
            33,
        ]

        # 1 to 33
        expected = []
        for x in range(1, 33 + 1):
            expected.append(x)

        result = recursive_flatten(data)

        assert result == expected
