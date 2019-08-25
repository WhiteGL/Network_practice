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