"""
Maximum Subarray Sum (Kadane's algorithm + variations)
"""

from typing import List


def max_subarray_sum(nums: list[int]) -> int:
    """Classic Kadane: max sum of contiguous subarray."""
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def max_subarray_sum_circular(nums: list[int]) -> int:
    """Max sum in circular array: either normal max subarray or total - min subarray."""
    total = sum(nums)
    best_max = cur_max = nums[0]
    best_min = cur_min = nums[0]
    for x in nums[1:]:
        cur_max = max(x, cur_max + x)
        best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)
    if best_min == total:  # all negative
        return best_max
    return max(best_max, total - best_min)


def max_subarray_sum_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """Returns (max_sum, start_index, end_index)."""
    best = cur = nums[0]
    start = end = 0
    cur_start = 0
    for i in range(1, len(nums)):
        x = nums[i]
        if cur + x > x:
            cur = cur + x
        else:
            cur = x
            cur_start = i
        if cur > best:
            best = cur
            start = cur_start
            end = i
    return best, start, end


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray_sum_circular([5, -3, 5]))  # 10
    print(max_subarray_sum_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # (6, 3, 6)
