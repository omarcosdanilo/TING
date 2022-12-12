from collections import deque


class Queue:
    def __init__(self):
        self.__data = deque()
        self.__position = 0

    def __repr__(self) -> str:
        return str(self.__data)

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self.__data[self.__position]
            self.__position += 1
        except IndexError:
            raise StopIteration()

        return value

    def enqueue(self, value):
        return self.__data.append(value)

    def dequeue(self):
        return self.__data.popleft()

    def search(self, index):
        if (index < 0) | (index > len(self.__data)):
            raise IndexError
        else:
            return self.__data[index]
