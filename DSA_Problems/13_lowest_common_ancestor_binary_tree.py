"""
Lowest Common Ancestor (Binary Tree)
Find the LCA of two nodes p and q (nodes are in the tree).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


if __name__ == "__main__":
    # Tree:      3
    #          /   \
    #         5     1
    #        / \   / \
    #       6   2 0   8
    #          / \
    #         7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left   # 5
    q = root.left.right.right  # 4
    lca = lowest_common_ancestor(root, p, q)
    print(lca.val if lca else None)  # 5
