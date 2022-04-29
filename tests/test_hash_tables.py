from datastructures_algorithms.hash_tables import intersection


class TestHashTables:
    def test_intersection(self):
        array1 = [1, 2, 3, 4, 5]
        array2 = [0, 2, 4, 6, 8]
        expected = [2, 4]

        assert intersection(array1, array2) == expected
