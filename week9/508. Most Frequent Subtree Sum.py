from collections import Counter
from typing import List, Optional


def find_frequent_tree_sum(root: Optional[tuple]) -> List[int]:
    def dfs(node):
        if not node:
            return 0
        subtree_sum = node[0] + dfs(node[1]) + dfs(node[2])
        counter[subtree_sum] += 1
        return subtree_sum

    counter = Counter()
    dfs(root)
    max_freq = max(counter.values())
    return [s for s in counter if counter[s] == max_freq]
