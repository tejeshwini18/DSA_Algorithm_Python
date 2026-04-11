class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        
        return -1

solution = Solution()
print(solution.findMiddleIndex([2, 3, -1, 8, 4]))
print(solution.findMiddleIndex([1, -1, 1]))
print(solution.findMiddleIndex([1, 2, 3]))
print(solution.findMiddleIndex([1, 2, 3, 4, 5]))
print(solution.findMiddleIndex([1, 2, 3, 4, 5, 6]))
print(solution.findMiddleIndex([1, 2, 3, 4, 5, 6, 7]))
print(solution.findMiddleIndex([1, 2, 3, 4, 5, 6, 7, 8]))
print(solution.findMiddleIndex([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution.findMiddleIndex([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))