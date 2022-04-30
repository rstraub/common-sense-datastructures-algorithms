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
        if self.__is_empty():
            return None
        return self.__data[-1]

    def pop(self):
        if self.__is_empty():
            return None
        return self.__data.pop()

    def __is_empty(self):
        return len(self.__data) == 0
