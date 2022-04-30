from datastructures_algorithms.hash_tables import (
    find_duplicate,
    find_missing_letter,
    find_non_duplicate_letter,
    intersection,
)


class TestHashTables:
    def test_intersection(self):
        array1 = [1, 2, 3, 4, 5]
        array2 = [0, 2, 4, 6, 8]
        expected = [2, 4]

        assert intersection(array1, array2) == expected

    def test_find_duplicate(self):
        chars = ["a", "b", "c", "d", "c", "e", "f"]

        assert find_duplicate(chars) == "c"

    def test_find_missing_letter(self):
        sentence = "The quick brown box jumps over the lazy dog"

        assert find_missing_letter(sentence) == "f"

    def test_find_non_duplicate_letter(self):
        word = "minimum"

        assert find_non_duplicate_letter(word) == "n"
