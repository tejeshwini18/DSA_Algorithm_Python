"""
Implement LFU Cache
Least Frequently Used cache. Evicts the least frequently used item.
Tie-break: least recently used among same frequency.
"""

from collections import defaultdict


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self) -> Node:
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node: dict[int, Node] = {}
        self.freq_to_list: dict[int, DLinkedList] = defaultdict(DLinkedList)

    def _update(self, node: Node) -> None:
        self.freq_to_list[node.freq].remove(node)
        if node.freq == self.min_freq and self.freq_to_list[node.freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_to_list[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update(node)
            return
        if len(self.key_to_node) >= self.capacity:
            evict = self.freq_to_list[self.min_freq].remove_last()
            del self.key_to_node[evict.key]
        node = Node(key, value)
        self.key_to_node[key] = node
        self.freq_to_list[1].add(node)
        self.min_freq = 1


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))   # 1
    cache.put(3, 3)       # evicts 2
    print(cache.get(2))   # -1
    print(cache.get(3))   # 3
    cache.put(4, 4)       # evicts 1
    print(cache.get(1))   # -1
    print(cache.get(3))   # 3
    print(cache.get(4))   # 4
