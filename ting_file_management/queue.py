from collections import deque


class Queue:
    def __init__(self):
        self.__data = deque()

    def __repr__(self) -> str:
        return str(self.__data)

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        return self.__data.append(value)

    def dequeue(self):
        return self.__data.popleft()

    def search(self, index):
        if (index < 0) | (index > len(self.__data)):
            raise IndexError
        else:
            return self.__data[index]
