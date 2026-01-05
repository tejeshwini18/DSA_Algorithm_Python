# A MinHeap is a binary heap where the parent node is always smaller than its child nodes. 
# This ensures that the smallest element is always at the root (heap[0]). The class uses an array to represent the heap structure.
class MinHeap:
    def __init__(self):
        # Creates an empty list self.heap to store the heap elements.
        self.heap = []

    def _left_child(self, index):
        # Purpose: Calculates the index of the left child of a node.
        # Behavior: For a node at index index, the left child is at index 2 * index + 1
        return 2 * index + 1

    def _right_child(self, index):
        # Purpose: Calculates the index of the right child of a node.
        # Behavior: For a node at index index, the right child is at index 2 * index + 2.
        return 2 * index + 2

    def _parent(self, index):
        # Purpose: Calculates the index of the parent of a node.
        # Behavior: For a node at index index, the parent is at index (index - 1) // 2
        return (index - 1) // 2

    def _swap(self, index1, index2):
        # Swaps the elements at two indices in the heap
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # Purpose: Inserts a new value into the heap while maintaining the heap property.
        # Behavior:
        # Appends the value to the end of the heap.
        # Compares the new value with its parent, swapping them if the parent is larger.
        # Repeats this process (called "bubble up") until the heap property is satisfied.
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self,index):
        # Purpose: Restores the heap property after removing the root.
        # Behavior:
        # Compares the value at index with its left and right children.
        # If a child is smaller than the current value, swaps the value with the smallest child.
        # Repeats this process (called "sink down") until the heap property is restored.
        min_index = index
        while True:
            left_index = self._left_child(min_index)
            right_index = self._right_child(min_index)
            
            if left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]:
                min_index = left_index
                
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
                min_index = right_index
                
            if min_index != index:
                self._swap(min_index,index)
                min_index = index
            else:
                return    

    def remove(self):
        # If the heap is empty, returns None.
        # If the heap has one element, removes and returns it.
        # Otherwise:
        # Removes the root and replaces it with the last element.
        # Sinks the new root down to restore the heap property.
        # Returns the original root (smallest value).
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value
        
        
        
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]



"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""