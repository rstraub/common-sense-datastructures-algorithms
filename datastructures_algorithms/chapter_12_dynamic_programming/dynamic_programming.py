def add_until_100(array):
    print("calculating")
    if len(array) == 0:
        return 0

    remainder = add_until_100(array[1 : len(array)])
    if array[0] + remainder > 100:
        return remainder
    else:
        return array[0] + remainder


_golomb_hits = 0


def golomb(n, memo={}):
    global _golomb_hits
    _golomb_hits += 1
    print("golomb hits: ", _golomb_hits)

    if n == 1:
        return 1

    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1)))
    return memo[n]


_path_hits = 0


def unique_paths(rows, columns, memo={}):
    global _path_hits
    _path_hits += 1
    print("unique paths hits: ", _path_hits)
    if rows == 1 or columns == 1:
        return 1

    if (rows, columns) not in memo:
        memo[rows, columns] = unique_paths(rows - 1, columns) + unique_paths(
            rows, columns - 1
        )

    return memo[(rows, columns)]
