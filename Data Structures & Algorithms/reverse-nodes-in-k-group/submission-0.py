# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previous_group_end = dummy
        reversing_pointer = head
        counting_pointer = head

        while counting_pointer:
            counter = k
            while counting_pointer and counter > 0:
                counting_pointer = counting_pointer.next
                counter -= 1
            
            if counter > 0:
                break
            counter = k

            next_start = counting_pointer
            prev = next_start
            group_start = reversing_pointer
            while reversing_pointer != next_start:
                temp = reversing_pointer.next
                reversing_pointer.next = prev
                prev = reversing_pointer
                reversing_pointer = temp
            
            previous_group_end.next = prev
            previous_group_end = group_start

        return dummy.next