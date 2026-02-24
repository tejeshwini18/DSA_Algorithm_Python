"""
Kth Largest Element in a Stream
Support add(val) and return the kth largest element. Use min-heap of size k.
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # 4
    print(kth.add(5))   # 5
    print(kth.add(10))  # 5
    print(kth.add(9))   # 8
    print(kth.add(4))   # 8
