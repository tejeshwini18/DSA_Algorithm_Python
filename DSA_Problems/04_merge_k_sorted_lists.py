"""
Merge K Sorted Lists
Merge k sorted linked lists into one sorted list.
O(N log k) where N = total nodes, k = number of lists.
"""

import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    heap: list[tuple[int, int, ListNode]] = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    dummy = ListNode(0)
    cur = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def list_to_nodes(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for x in arr[1:]:
        cur.next = ListNode(x)
        cur = cur.next
    return head


def nodes_to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    lists = [
        list_to_nodes([1, 4, 5]),
        list_to_nodes([1, 3, 4]),
        list_to_nodes([2, 6]),
    ]
    merged = merge_k_lists(lists)
    print(nodes_to_list(merged))  # [1, 1, 2, 3, 4, 4, 5, 6]
