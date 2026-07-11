# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = l1
        cur_2 = l2
        carry = 0
        result = node = ListNode()
        while cur_1 or cur_2 or carry:
            digit_1 = cur_1.val if cur_1 else 0
            digit_2 = cur_2.val if cur_2 else 0
            total = digit_1 + digit_2 + carry            
            value = total % 10      
            carry = total // 10

            if cur_1:
                cur_1 = cur_1.next
            if cur_2:
                cur_2 = cur_2.next

            node.next = ListNode(value)
            node = node.next
        
        return result.next
