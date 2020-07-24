class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node == None:
            self.head = node
            return
        self.reverse_list(node.get_next(), prev)
        temp = node.get_next()
        temp.set_next(node)
        node.set_next(None)


LL = LinkedList()
LL.add_to_head(1)
LL.reverse_list(LL.head, LL.head.get_next())

#
#is there a node? return if there is
#if a node is not the head keep traversing
#make the last node the head if next is None
#give set_next the "prev" val => set_next(prev) or get_next(prev)
#can i figure out iteratively?

