"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            node_copy = Node(cur.val)
            node_copy.next = cur.next
            cur.next = node_copy
            cur = node_copy.next

        cur = head
        while cur:
            node_copy = cur.next
            node_copy.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur = head
        head = head.next
        while cur:
            temp = cur.next
            cur.next = cur.next.next if cur.next else None
            node_copy = temp
            node_copy.next = node_copy.next.next if node_copy.next else None
            cur = cur.next

        return head
            

            