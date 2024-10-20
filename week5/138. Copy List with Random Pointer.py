class Node:
    def __init__(self, val: int, next: "Node" = None, random: "Node" = None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head: "Node") -> "Node":
    if not head:
        return None

    # Step 1: Create new nodes interleaved with the original nodes
    current = head
    while current:
        new_node = Node(current.val, current.next, None)
        current.next = new_node
        current = new_node.next

    # Step 2: Set random pointers for the new nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original and copied lists
    old_list = head
    new_list = head.next
    new_head = head.next

    while old_list:
        old_list.next = old_list.next.next
        if new_list.next:
            new_list.next = new_list.next.next
        old_list = old_list.next
        new_list = new_list.next

    return new_head
