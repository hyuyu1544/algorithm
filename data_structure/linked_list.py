"""Linked list.
advantage:
.. time complexity is O(1) when insert and deletion of elements

ref: https://realpython.com/linked-lists-python/
"""


def linked_list_collections_deque():
    """
    deque('abc')==deque(['a','b','c'])
    deque([{'data': 'a'}, {'data': 'b'}])
    """
    from collections import deque
    llist = deque("abcde")
    llist.append(f)
    llist.pop()
    print(llist)
    llist.appendleft("z")
    llist.poplist()

# ==============================================
# implements linked list by myself


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# def run():
# 要自己去指下一個點在哪
listedlist = LinkedList()
first_node = Node("a")
listedlist.head = first_node
second_node = Node("b")
first_node.next = second_node
third_node = Node("c")
second_node.next = third_node


# ============================================
# 進化版linkedlist


class LinkedList_V2:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:  # because has __repr__, self = a -> b -> None
            pass
        current_node.next = node

    def add_after(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty.")

        for current_node in self:
            if current_node.data == target_node:
                new_node.next = current_node.next
                current_node.next = new_node
                return

        raise Exception(f'Node with data `{target_node}` not found.')

    def add_before(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty.")

        if self.head.data == target_node:
            return self.add_first(new_node)

        pre_node = self.head
        for current_node in self:
            if current_node.data == target_node:
                pre_node.next = new_node
                new_node.next = current_node
                return
            pre_node = current_node

        raise Exception(f'Node with data `{target_node}` not found.')

    def remove_node(self, node):
        if not self.head:
            raise Exception("List is empty.")

        if self.head.data == node:
            self.head = self.head.next
            return

        pre_node = self.head
        for current_node in self:
            if current_node.data == node:
                pre_node.next = current_node.next
                return
            pre_node = current_node

        raise Exception(f'Node with data `{node}` not found.')

    def get_node_position(self, node):
        """Create a method to retrieve an element from a specific position: get(i) or even llist[i]."""
        if not self.head:
            raise Exception('List is empty')
        no = 0
        for current_node in self:
            no += 1
            if current_node.data == node:
                return no
        raise Exception(f'Node with data `{node}` not found.')

    def reverse(self):
        """Create a method to reverse the linked list: llist.reverse()."""
        if not self.head:
            raise Exception('List is empty')
        pre_node = None
        node = self.head
        while node is not None:
            current_node = node
            node = node.next
            current_node.next = pre_node
            pre_node = current_node
        return pre_node

    # TODO::Create a Queue() object inheriting this article’s linked list with enqueue() and dequeue() methods.


llist = LinkedList_V2()
llist.add_first(Node("b"))
llist.add_first(Node("a"))
llist.add_last(Node("c"))
llist.add_after('b', Node('bb'))
llist.add_before('c', Node('cc'))
llist.remove_node('bb')
