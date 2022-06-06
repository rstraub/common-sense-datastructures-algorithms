from datastructures_algorithms.chapter_12_dynamic_programming.dynamic_programming import (
    add_until_100,
    golomb,
    unique_paths,
)


class TestDynamicProgramming:
    def test_add_until_100(self):
        result = add_until_100([20, 30, 60, 45])
        assert result == 95

    def test_golomb(self):
        assert golomb(7) == 4

    def test_unique_paths(self):
        assert (unique_paths(3, 7)) == 28
