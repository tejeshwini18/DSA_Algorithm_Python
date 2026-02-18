"""
Word Ladder - Shortest transformation from beginWord to endWord.
Each step change one letter; every intermediate word must be in wordList.
BFS for shortest path.
"""

from collections import deque


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    q: deque[tuple[str, int]] = deque([(begin_word, 1)])
    seen = {begin_word}
    while q:
        word, steps = q.popleft()
        if word == end_word:
            return steps
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == word[i]:
                    continue
                nw = word[:i] + c + word[i + 1:]
                if nw in word_set and nw not in seen:
                    seen.add(nw)
                    q.append((nw, steps + 1))
    return 0


if __name__ == "__main__":
    print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(ladder_length("a", "c", ["a", "b", "c"]))  # 2
    print(ladder_length("hot", "dog", ["hot", "dog"]))  # 0
