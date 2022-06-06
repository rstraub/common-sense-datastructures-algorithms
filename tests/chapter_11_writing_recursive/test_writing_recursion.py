from datastructures_algorithms.chapter_11_writing_recursive.writing_recursive import (
    count_chars,
)


class TestWritingRecursion:
    def test_count_chars_should_return_total_chars_given_more_than_one_text(self):
        texts = ["ab", "c", "def", "ghij"]

        result = count_chars(texts)

        assert result == 10

    def test_count_chars_should_return_0_given_empty_list(self):
        assert count_chars([]) == 0
