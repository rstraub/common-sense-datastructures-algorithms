def add_until_100(array):
    print("calculating")
    if len(array) == 0:
        return 0

    remainder = add_until_100(array[1 : len(array)])
    if array[0] + remainder > 100:
        return remainder
    else:
        return array[0] + remainder


def golomb(n, memo={}):
    print("golomb")

    if n == 1:
        return 1

    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1)))
    return memo[n]
