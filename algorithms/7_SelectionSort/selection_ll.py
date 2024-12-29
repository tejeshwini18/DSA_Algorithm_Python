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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def selection_sort(self):
        if self.length <= 1:
            return

        for i in range(self.length - 1):
            min_index = i
            current = self.head
            current_index = 0
            
            while current is not None:
                if current_index > i and current.value < self.get_node_value(min_index):
                    min_index = current_index
                current = current.next
                current_index += 1
                
            # Swap the found minimum element with the first element of the unsorted part
            if min_index != i:
                self.swap_nodes(i, min_index)

    def get_node_value(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def swap_nodes(self, index1, index2):
        if index1 == index2:
            return
        
        # Get references to the nodes to be swapped
        node1 = self.head
        for _ in range(index1):
            node1 = node1.next
        
        node2 = self.head
        for _ in range(index2):
            node2 = node2.next
            
        # Swap values of the nodes (instead of swapping nodes)
        node1.value, node2.value = node2.value, node1.value



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

