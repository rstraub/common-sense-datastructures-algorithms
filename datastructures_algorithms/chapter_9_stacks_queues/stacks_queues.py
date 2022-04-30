from datastructures_algorithms.chapter_9_stacks_queues.stack import Stack


def reverse(sentence):
    stack = Stack()
    for letter in sentence:
        stack.push(letter)

    result = ""
    while stack.read():
        result += stack.pop()

    return result
