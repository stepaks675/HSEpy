from typing import Optional


def rob(root: Optional[tuple]) -> int:
    def dfs(node):
        if not node:
            return (0, 0)  # (max if not robbed, max if robbed)
        left = dfs(node[1])
        right = dfs(node[2])
        rob_current = node[0] + left[0] + right[0]
        not_rob_current = max(left) + max(right)
        return (not_rob_current, rob_current)

    return max(dfs(root))
