class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            return print("empty stack")

    def is_empty(self):
        return bool(self.stack)

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[len(self.stack) - 1]


class ClassicStack(object):
    def __init__(self):
        self.max_size = 100
        self.stack = [0] * self.max_size
        self.base = 0
        self.top = 0

    def push(self, data):
        self.stack[self.top] = data
        self.top += 1

    def pop(self):
        if self.top == self.base:
            return print("empty stack")
        else:
            elem = self.stack[self.top - 1]
            self.top -= 1
            self.stack[self.top] = 0
            return elem

    def clear(self):
        self.top = self.base

    def size(self):
        return self.top - self.base

    def peak(self):
        if self.top == self.base:
            return print("empty stack")
        else:
            return self.stack[self.top - 1]

    def is_empty(self):
        return self.top == self.base
