from datastructures_algorithms.step_printer import print_steps


def intersection(array1, array2):
    steps = 0
    result = []
    temp = {}

    for item in array1:
        temp[item] = True
        steps += 1

    for item in array2:
        if item in temp:
            result.append(item)
        steps += 1

    print_steps("intersection", steps)

    return result
