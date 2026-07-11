# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        reversed_half = None
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = reversed_half
            reversed_half = cur
            cur = temp
        
        while reversed_half:
            temp_1 = head.next
            temp_2 = reversed_half.next

            head.next = reversed_half
            reversed_half.next = temp_1

            head = temp_1
            reversed_half = temp_2

        