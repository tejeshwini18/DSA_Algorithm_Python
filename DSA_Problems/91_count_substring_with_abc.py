class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {'a': 0, 'b': 0, 'c': 0}
        ans = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += len(s) - right
                count[s[left]] -= 1
                left += 1

        return ans


print(Solution().numberOfSubstrings("abcabc"))
print(Solution().numberOfSubstrings("abc"))
print(Solution().numberOfSubstrings("a"))
print(Solution().numberOfSubstrings("b"))
print(Solution().numberOfSubstrings("c"))
print(Solution().numberOfSubstrings("ab"))
print(Solution().numberOfSubstrings("ac"))
print(Solution().numberOfSubstrings("bc"))
print(Solution().numberOfSubstrings("abc"))
print(Solution().numberOfSubstrings("abcabc"))
print(Solution().numberOfSubstrings("abcabc"))