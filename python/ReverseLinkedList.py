# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        temp = head
        res = None
        while(temp):
            if(temp.next == None):
                res = temp
            x = temp.next
            temp.next = prev
            prev = temp
            temp = x
            
        return res