import pytest

from datastructures_algorithms.chapter_11_writing_recursive.writing_recursive import (
    count_chars,
    select_even,
    triangle,
)


class TestWritingRecursion:
    def test_count_chars(self):
        texts = ["ab", "c", "def", "ghij"]

        result = count_chars(texts)

        assert result == 10

    def test_select_even(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        result = select_even(numbers)

        assert result == [2, 4, 6, 8]

    @pytest.mark.parametrize(
        "n,expected", [(1, 1), (2, 3), (3, 6), (4, 10), (5, 15), (6, 21), (7, 28)]
    )
    def test_triangle(self, n, expected):
        assert triangle(n) == expected
