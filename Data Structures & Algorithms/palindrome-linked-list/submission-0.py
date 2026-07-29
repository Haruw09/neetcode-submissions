# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None
        reversed_head = head
        while fast and fast.next:
            slow = slow.next
            temp = slow
            fast = fast.next.next

            reversed_head.next = prev
            prev = reversed_head
            reversed_head = temp

        if not fast:
            reversed_head = prev
        else:
            slow = slow.next
            reversed_head = prev

        while slow and reversed_head: 
            if slow.val != reversed_head.val:
                return False
            slow = slow.next
            reversed_head = reversed_head.next

        return True

        