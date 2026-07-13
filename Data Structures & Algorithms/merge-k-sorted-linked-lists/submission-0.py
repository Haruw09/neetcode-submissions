import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for list_idx, node in enumerate(lists):
            if node:
                value = node.val
                heapq.heappush(heap, (value, list_idx, node))

        dummy = cur = ListNode()
        while heap:
            _, list_idx, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
            
            cur.next = node
            cur = cur.next

        return dummy.next
