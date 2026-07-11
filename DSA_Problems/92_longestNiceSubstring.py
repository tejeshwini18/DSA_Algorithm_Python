from typing import List

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                st = set(sub)

                nice = True
                for ch in st:
                    if ch.swapcase() not in st:
                        nice = False
                        break

                if nice and len(sub) > len(ans):
                    ans = sub

        return ans

print(Solution().longestNiceSubstring("YazaAay"))
print(Solution().longestNiceSubstring("Bb"))
print(Solution().longestNiceSubstring("CbC"))
print(Solution().longestNiceSubstring("c"))
print(Solution().longestNiceSubstring("d"))
print(Solution().longestNiceSubstring("e"))
print(Solution().longestNiceSubstring("f"))
print(Solution().longestNiceSubstring("g"))
print(Solution().longestNiceSubstring("h"))
print(Solution().longestNiceSubstring("i"))
print(Solution().longestNiceSubstring("j"))