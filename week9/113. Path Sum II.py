from typing import List, Optional


def path_sum(root: Optional[tuple], targetSum: int) -> List[List[int]]:
    def dfs(node, current_sum, path):
        if not node:
            return
        current_sum += node[0]
        path.append(node[0])
        if not node[1] and not node[2] and current_sum == targetSum:
            result.append(path[:])
        dfs(node[1], current_sum, path)
        dfs(node[2], current_sum, path)
        path.pop()

    result = []
    dfs(root, 0, [])
    return result
