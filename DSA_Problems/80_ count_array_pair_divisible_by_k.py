from collections import defaultdict
from math import gcd

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0

        for num in nums:
            g = gcd(num, k)

            for prev_g in freq:
                if (g * prev_g) % k == 0:
                    count += freq[prev_g]

            freq[g] += 1

        return count

solution = Solution()
print(solution.countPairs([1,2,3,4,5], 2))
print(solution.countPairs([1,2,3,4,5], 3))
print(solution.countPairs([1,2,3,4,5], 4))
print(solution.countPairs([1,2,3,4,5], 5))
print(solution.countPairs([1,2,3,4,5], 6))
print(solution.countPairs([1,2,3,4,5], 7))
print(solution.countPairs([1,2,3,4,5], 8))
print(solution.countPairs([1,2,3,4,5], 9))
print(solution.countPairs([1,2,3,4,5], 10))
