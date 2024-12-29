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

    def insertion_sort(self):
        if self.length <= 1:
            return
        
        sorted_head = None  # This will be the head of the sorted list
        current = self.head
        
        while current is not None:
            # At each iteration, we will insert current into the sorted list
            next_node = current.next  # Save the next node for the next iteration
            if sorted_head is None or current.value < sorted_head.value:
                # Insert at the beginning of the sorted portion
                current.next = sorted_head
                sorted_head = current
            else:
                # Find the appropriate spot to insert
                sorted_temp = sorted_head
                while (sorted_temp.next is not None and 
                       sorted_temp.next.value < current.value):
                    sorted_temp = sorted_temp.next
                
                # Insert current in the correct position
                current.next = sorted_temp.next
                sorted_temp.next = current
            # Move to the next node
            current = next_node
        self.head = sorted_head  # Update head to the new sorted list




my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

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

