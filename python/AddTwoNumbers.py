# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resLL = ListNode()
        currNode = resLL

        carry = 0 

        while(l1 != None or l2 != None):

            sum = carry

            if(l1 != None):
                sum+=l1.val
                l1 = l1.next
            if(l2 != None):
                sum+=l2.val
                l2 = l2.next
            carry = sum // 10
            sum = sum % 10
            
            currNode.next = ListNode(sum)
            currNode = currNode.next
            
        if carry == 1:
            currNode.next = ListNode(1)
            
        return resLL.next