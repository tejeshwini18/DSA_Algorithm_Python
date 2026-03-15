"""
Maximum Subarray Sum (Kadane's algorithm + variations)
"""

from typing import List

def max_subarray_sum(nums: list[int]) -> int:
    max_current = max_global = nums[0]
    for x in nums[1:]:
        max_current = max(x, max_current + x)
        max_global = max(max_global, max_current)
    return max_global


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
