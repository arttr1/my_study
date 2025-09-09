# Реализация стека (Stack)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

# Реализация очереди (Queue)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def size(self):
        return len(self.items)

# Реализация дека (Deque)
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop()

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop(0)

    def size(self):
        return len(self.items)



# =================================


# Базовый класс Memory
class Memory:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def add(self, item):
        raise NotImplementedError("Метод add должен быть реализован в дочернем классе")

    def remove(self):
        raise NotImplementedError("Метод remove должен быть реализован в дочернем классе")

# Реализация стека (Stack)
class Stack(Memory):
    def __init__(self):
        super().__init__()

    def add(self, item):
        self.items.append(item)  # Добавление в конец

    def remove(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()  # Удаление с конца

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

# Реализация очереди (Queue)
class Queue(Memory):
    def __init__(self):
        super().__init__()

    def add(self, item):
        self.items.append(item)  # Добавление в конец

    def remove(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)  # Удаление с начала

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

# Реализация дека (Deque)
class Deque(Memory):
    def __init__(self):
        super().__init__()

    def add_front(self, item):
        self.items.append(item)  # Добавление в конец

    def add_rear(self, item):
        self.items.insert(0, item)  # Добавление в начало

    def remove_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop()  # Удаление с конца

    def remove_rear(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.items.pop(0)  # Удаление с начала
