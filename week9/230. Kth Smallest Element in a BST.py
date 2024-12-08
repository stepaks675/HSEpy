from typing import Optional


def kth_smallest(root: Optional[tuple], k: int) -> int:
    def inorder(node):
        if not node:
            return []
        return inorder(node[1]) + [node[0]] + inorder(node[2])

    return inorder(root)[k - 1]
