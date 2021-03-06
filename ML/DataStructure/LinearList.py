class Node(object):
    # 单向链表节点
    def __init__(self, data, l_next=None):
        self.data = data
        self.next = l_next

    def __repr__(self):
        return str(self.data)


# 链表类
class LinearList(object):
    def __init__(self, data=Node):
        head = Node(data)
        self.head = head
        self.length = 0

    # 判空函数
    def isEmpty(self):
        return self.length == 0

    # 增加节点
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.length += 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
            self.length += 1

    # 删除节点
    def delete(self, target):
        if target > self.length:
            return print("out of range")
        elif target == self.length:
            pos = 0
            node = self.head
            while pos < target - 1:
                node = node.next
                pos += 1
            node.next = None
        else:
            pos = 0
            node = self.head
            while pos < target - 1:
                node = node.next
                pos += 1
            node2 = node.next
            node.next = node2.next
            return 0

    # 插入节点
    def insert(self, data, target):
        if target > self.length:
            return print("out of range")
        elif target == self.length:
            pos = 0
            node = self.head
            while pos < target:
                node = node.next
                pos += 1
            node.next = Node(data)
        else:
            pos = 0
            node = self.head
            while pos < target:
                node = node.next
                pos += 1
            new_node = Node(data)
            node2 = node.next
            node.next = new_node
            new_node.next = node2

    # 清空链表
    def clear(self):
        self.head = None
        self.length = 0

    # 按索引获取元素
    def getElem(self, target):
        pos = 0
        node = self.head
        while pos < target:
            node = node.next
            pos += 1
        return node.data

    # 获取指定元素的位置
    def loc(self, elem):
        pos = 0
        node = self.head
        while node:
            if node.data == elem:
                return pos
            else:
                node = node.next
                pos += 1
        return -1


test = LinearList()
for i in range(10):
    test.append(i)

print(test.loc(3))
print(test.loc(11))