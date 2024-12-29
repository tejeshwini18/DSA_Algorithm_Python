# 1. Initialization (__init__):
# Explanation: When we create a linked list, we start with a single node (the head) that holds a value. This node also serves as the tail because it's the only node in the list initially. We keep track of the length of the list to make operations easier.

# 2. Print List (print_list):
# Explanation: This operation traverses the list starting from the head and prints each node's value. It's like walking through a line of people and reading their names.

# 3. Append (append):
# Explanation: To add a new item at the end of the list, we create a new node and make the current tail point to it. The new node becomes the tail. If the list is empty, the new node becomes both the head and the tail.

# 4. Pop (pop):
# Explanation: To remove the last item, we traverse the list to find the second-to-last node. This node becomes the new tail, and its pointer to the last node is removed. If there's only one node, the list becomes empty.

# 5. Prepend (prepend):
# Explanation: To add a new item at the beginning, we create a new node and point it to the current head. The new node becomes the head. If the list is empty, the new node becomes both the head and the tail.

# 6. Pop First (pop_first):
# Explanation: To remove the first item, we move the head pointer to the second node in the list. If there’s only one node, the list becomes empty.

# 7. Get (get):
# Explanation: To retrieve a node at a specific position, we traverse the list from the head, counting as we go until we reach the desired index.

# 8. Set Value (set_value):
# Explanation: To update a node's value, we first find the node using its index and then change its value to the new one.

# 9. Insert (insert):
# Explanation: To add a new node at a specific position:
# If it's at the beginning, we use prepend.
# If it's at the end, we use append.
# Otherwise, we find the node before the desired position, point the new node to the next node, and update the previous node to point to the new one.

# 10. Remove (remove):
# Explanation: To delete a node:
# If it’s the first node, we use pop_first.
# If it’s the last node, we use pop.
# Otherwise, we find the node before the one to be removed, update its pointer to skip the unwanted node, and disconnect the unwanted node.

# 11. Reverse (reverse):
# Explanation: To reverse the list, we flip the direction of the pointers between nodes. The head becomes the tail, and the tail becomes the head. It’s like flipping a chain of dominoes.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""