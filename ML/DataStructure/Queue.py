class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkQueue(object):
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear:
            temp = self.rear
            temp.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        if self.front and (self.front != self.rear):
            temp = self.front
            self.front = temp.next
            return temp.data
        elif self.front and (self.front == self.rear):
            temp = self.front
            self.front = None
            self.rear = None
            return temp.data
        else:
            raise LookupError('empty queue')

    def size(self):
        length = 0
        front = self.front
        while front:
            length += 1
            front = front.next
        return length

    def is_empty(self):
        if self.front:
            return False
        else:
            return True

    def clear(self):
        self.front = None
        self.rear = None

    def top(self):
        if self.front:
            return self.front.data
        else:
            raise LookupError('empty queue')


test = LinkQueue()
for i in range(10):
    test.enqueue(i)
print(test.size())
print(test.dequeue())
print(test.size())
print(test.top())