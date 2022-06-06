from datastructures_algorithms.chapter_12_dynamic_programming.dynamic_programming import (
    add_until_100,
)


class TestDynamicProgramming:
    def test_add_until_100(self):
        result = add_until_100([20, 30, 60, 45])
        assert result == 95
