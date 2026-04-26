class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i]==nums[j]:
                    count += abs(i-j)
            result.append(count)
        return result

s = Solution()
print(s.distance([1,3,1,1,2]))