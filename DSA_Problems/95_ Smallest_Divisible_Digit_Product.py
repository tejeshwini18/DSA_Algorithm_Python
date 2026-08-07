class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if t == 0:
            if n == 1:
                return 0
            else:
                return -1
        for num in range(n,101):
            prod = 1
            for digit in str(num):
                prod *= int(digit)
            if prod%t==0:
                return num

sol = Solution()
print(sol.smallestNumber(2, 2))
print(sol.smallestNumber(2, 3))
print(sol.smallestNumber(3, 0))
print(sol.smallestNumber(3, 5))
print(sol.smallestNumber(3, 6))
print(sol.smallestNumber(3, 7)) 
print(sol.smallestNumber(3, 8))
print(sol.smallestNumber(3, 9))