"""
Serialize & Deserialize Binary Tree
Encode to string and decode back to tree (e.g. level-order with "null" for missing).
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q: deque[Optional[TreeNode]] = deque([root])
        parts = [str(root.val)]
        while q:
            node = q.popleft()
            if not node:
                continue
            for child in (node.left, node.right):
                if child:
                    parts.append(str(child.val))
                    q.append(child)
                else:
                    parts.append("null")
                    q.append(None)
        while parts and parts[-1] == "null":
            parts.pop()
        return ",".join(parts)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        parts = data.split(",")
        root = TreeNode(int(parts[0]))
        q: deque[TreeNode] = deque([root])
        i = 1
        while q and i < len(parts):
            node = q.popleft()
            if i < len(parts) and parts[i] != "null":
                node.left = TreeNode(int(parts[i]))
                q.append(node.left)
            i += 1
            if i < len(parts) and parts[i] != "null":
                node.right = TreeNode(int(parts[i]))
                q.append(node.right)
            i += 1
        return root


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    codec = Codec()
    s = codec.serialize(root)
    print(s)
    back = codec.deserialize(s)
    print(codec.serialize(back) == s)
