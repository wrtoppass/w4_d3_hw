from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None # it also means False, null

    def add_node(self, value):
        node = Node(value)
        if not self.head: # this turn it into True
            self.head = node
            return
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = node

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def __repr__(self):
        return ' -> '.join(node.value for node in self)
        # nodes = []
        # for node in self:
        #     nodes.append(node.value)
        # return' -> '.join(nodes)

    def insert_node(self, target, value):
        new_node = Node(value)
        if self.head:
            for node in self:
                if node.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print('Empty List')

    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else: 
            for node in self:
               if node.right.value == value:
                node.right = node.right.right 
                return

    def insert_before(self, target, value):
        new_node = Node(value)
        if self.head.value == target:
            right_node = self.head
            self.head = new_node
            new_node.right = right_node
        for node in self:
            if node.right.value == target:
                right_node = node.right
                node.right = new_node
                new_node.right = right_node
                return
        else:
            print("empty list")

    def get_tail(self):
        # for node in self:
        #     pass
        # return node
        node = self.head
        while node.right:
            node = node.right
        return node.value

    def remove_tail(self):
        node = self.head
        if node.right:
            while node.right.right:
                node = node.right
            node.right = None

    def add_list_elements(self, a_list):
        for e in a_list:
            self.add_node(str(e))

# linked_list = LinkedList()

# linked_list.add_list_elements([1,2,3,4,5])

# print(linked_list)

# linked_list.add_node('Sunday')
# linked_list.add_node('Monday')
# linked_list.add_node('Tuesday')
# linked_list.add_node('Thursday')

# print(linked_list)

# # linked_list.insert_node('Tuesday', 'Wednesday')

# # print(linked_list)

# linked_list.add_node('Spazday')

# print(linked_list)

# linked_list.remove_node('Sunday')

# print(linked_list)

# linked_list.remove_tail()
# print(linked_list)


# node = Node(1)
# node.right = Node(2)
# second_node = node.right
# node.right.right = Node(3)

# print(node.right.right.value)