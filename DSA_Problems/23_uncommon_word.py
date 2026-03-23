from collections import Counter
from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        freq = Counter(words)

        return [word for word in freq if freq[word] == 1]

sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
result = sol.uncommonFromSentences(s1,s2)
print(result)