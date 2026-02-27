"""
Top K Frequent Elements
Return k most frequent elements. Bucket sort or heap.
"""

from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    # Min-heap of size k: (freq, num). Keep k largest by freq.
    heap: list[tuple[int, int]] = []
    for num, freq in count.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heapq.heapreplace(heap, (freq, num))
    return [num for _, num in heap]


def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    n = len(nums)
    buckets: list[list[int]] = [[] for _ in range(n + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for freq in range(n, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(top_k_frequent_bucket([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
