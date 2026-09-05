class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix_min[i] = minimum value from index i to n-1
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Maximum value from index 0 to i
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            instability = prefix_max - suffix_min[i]

            if instability <= k:
                return i

        return -1


# Example usage
solution = Solution()

tests = [
    ([2, 5, 3, 8], 2, 0),
    ([5, 0, 1, 4], 3, 3),
    ([3, 2, 1], 1, -1),
    ([7], 0, 0),
    ([4, 2, 4, 3], 0, -1),
    ([5, 5, 5, 5], 0, 0),
    ([1, 2, 3, 4, 5], 2, 0),
    ([10, 8, 6, 4, 2], 3, -1),
    ([10, 3, 7, 8], 5, 2),
    ([1, 10, 2, 9, 3], 2, 4),
]

for nums, k, expected in tests:
    result = solution.firstStableIndex(nums, k)
    print(f"firstStableIndex({nums}, {k}) = {result}, expected = {expected}")
