"""
Design a Task Scheduler with Priorities
Schedule tasks with cooldown n; same task must be n apart. Priority by frequency.
"""

from collections import Counter
import heapq
from typing import Optional


class TaskScheduler:
    """Schedule with cooldown: same task cannot run within n slots."""

    def __init__(self, n: int):
        self.n = n

    def least_interval(self, tasks: list[str]) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        num_max = sum(1 for v in count.values() if v == max_freq)
        # At least (max_freq - 1) * (n + 1) + num_max slots
        return max(len(tasks), (max_freq - 1) * (self.n + 1) + num_max)


class PriorityTaskScheduler:
    """Min-heap by (next_available_time, -priority). Priority = higher freq = higher priority."""

    def __init__(self, cooldown: int):
        self.cooldown = cooldown
        self.time = 0
        self.freq: dict[str, int] = {}
        self.heap: list[tuple[int, int, str]] = []  # (next_time, -freq, task)

    def add_task(self, task: str, count: int = 1) -> None:
        self.freq[task] = self.freq.get(task, 0) + count

    def schedule_next(self) -> Optional[tuple[int, str]]:
        """Returns (time_scheduled, task) or None if no tasks."""
        if not self.freq:
            return None
        # Build heap: (next_available, -freq, task)
        self.heap = []
        for task, f in self.freq.items():
            next_t = 0
            self.heap.append((next_t, -f, task))
        heapq.heapify(self.heap)
        result = []
        while self.heap and len(result) < sum(self.freq.values()):
            next_t, neg_f, task = heapq.heappop(self.heap)
            self.time = max(self.time, next_t)
            result.append((self.time, task))
            self.freq[task] -= 1
            if self.freq[task] == 0:
                del self.freq[task]
            else:
                heapq.heappush(
                    self.heap,
                    (self.time + self.cooldown + 1, -self.freq[task], task),
                )
            self.time += 1
        return result[0] if result else None


if __name__ == "__main__":
    sched = TaskScheduler(2)
    print(sched.least_interval(["A", "A", "A", "B", "B", "B"]))  # 8
    print(sched.least_interval(["A", "A", "A", "B", "B", "B", "C", "C", "C"]))  # 9
