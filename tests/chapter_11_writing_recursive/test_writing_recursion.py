from datastructures_algorithms.chapter_11_writing_recursive.writing_recursive import (
    count_chars,
    select_even,
)


class TestWritingRecursion:
    def test_count_chars_should_return_total_chars(self):
        texts = ["ab", "c", "def", "ghij"]

        result = count_chars(texts)

        assert result == 10

    def test_select_even_should_return_even_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        result = select_even(numbers)

        assert result == [2, 4, 6, 8]
