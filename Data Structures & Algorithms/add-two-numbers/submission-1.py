# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = node = ListNode()
        while l1 or l2 or carry:
            digit_1 = l1.val if l1 else 0
            digit_2 = l2.val if l2 else 0
            total = digit_1 + digit_2 + carry            
            value = total % 10      
            carry = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            node.next = ListNode(value)
            node = node.next
        
        return result.next
