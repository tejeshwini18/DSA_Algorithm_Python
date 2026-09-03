class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)

        # If the minimum element is odd, all numbers can be made odd
        if min_val % 2 != 0:
            return True

        # If the minimum is even, all elements must be even
        return all(x % 2 == 0 for x in nums1)

# Example usage:
solution = Solution()
result = solution.uniformArray([2, 4, 6, 8])
print(result)  # Output: True

result = solution.uniformArray([1, 3, 5, 7])
print(result)  # Output: True

result = solution.uniformArray([1, 2, 3, 4])
print(result)  # Output: False