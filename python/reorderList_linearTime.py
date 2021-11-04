# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head.next 
        first = slow

        # find mid and end
        while (fast and fast.next):
            slow = slow.next 
            fast = fast.next.next

        second = slow.next 
        slow.next = None
        prev = None 
        # reverse second half
        while second:
            temp = second.next 
            temp.next = prev 
            prev = temp
            second = temp
        
        #merge lists 
        while second:
            first.next = second
            first = first.next 
            second = second.next

        first.next = None
       
            
# Even length 1->2->3->4
# expected = 1->4->2->3

# Odd length  1->2->3->4->5
# expected = 1->5->2->4->3

# empty set None
# expected = None 