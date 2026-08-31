from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Make sure min_idx is the leftmost position
        # and max_idx is the rightmost position.
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Remove both from the left
        remove_left = right + 1

        # 2. Remove both from the right
        remove_right = n - left

        # 3. Remove left element from left
        #    and right element from right
        remove_both = (left + 1) + (n - right)

        return min(remove_left, remove_right, remove_both)

# Example usage:
solution = Solution()
result = solution.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6])
print(result)  # Output: 5  

result = solution.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5])
print(result)  # Output: 3

result = solution.minimumDeletions([101])
print(result)  # Output: 1

result = solution.minimumDeletions([1, 2, 3])
print(result)  # Output: 2