"""
Minimum Window Substring
Smallest substring of s that contains all characters of t (with frequencies).
Sliding window + two maps (need, have).
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    need = Counter(t)
    have = 0
    required = len(need)
    window: dict[str, int] = {}
    best_len = float("inf")
    best_start = 0
    left = 0
    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            have += 1
        while have == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_start = left
            lc = s[left]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                have -= 1
            left += 1
    return s[best_start : best_start + best_len] if best_len != float("inf") else ""


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    print(min_window("a", "a"))                # "a"
    print(min_window("a", "aa"))               # ""
