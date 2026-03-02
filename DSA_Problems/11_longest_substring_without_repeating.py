"""
Longest Substring Without Repeating Characters
Sliding window + set to track characters in window.
"""

def length_of_longest_substring(s: str) -> int:
    seen: set[str] = set()
    left = 0
    best = 0
    for right, c in enumerate(s):
        while c in seen:
            seen.discard(s[left])
            left += 1
        seen.add(c)
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
