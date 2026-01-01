class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data, node_class=Node):
        old_head = self.head
        self.head = node_class(data, old_head)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data



