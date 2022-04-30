class Queue:
    def __init__(self):
        self.__data = []

    def read(self):
        return None if self.__is_empty() else self.__data[-1]

    def enqueue(self, element):
        self.__data.insert(0, element)

    def dequeue(self):
        return None if self.__is_empty() else self.__data.pop()

    def __is_empty(self):
        return len(self.__data) == 0
