from typing import Optional


def sum_numbers(root: Optional[tuple]) -> int:
    def dfs(node, current_number):
        if not node:
            return 0
        current_number = current_number * 10 + node[0]
        if not node[1] and not node[2]:
            return current_number
        return dfs(node[1], current_number) + dfs(node[2], current_number)

    return dfs(root, 0)
