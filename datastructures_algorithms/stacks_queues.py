def reverse(sentence):
    stack = Stack()
    for letter in sentence:
        stack.push(letter)

    result = ""
    while stack.read():
        result += stack.pop()

    return result


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, letter):
        self.__data.append(letter)

    def read(self):
        if len(self.__data) > 0:
            return self.__data[-1]
        return None

    def pop(self):
        return self.__data.pop()
