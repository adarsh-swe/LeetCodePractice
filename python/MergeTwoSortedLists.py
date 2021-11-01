# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()   
        currNode = res

        while(l1 != None or l2 != None):
            if(l1 != None and l2 != None): #when both lists non empty 
                if(l1.val <= l2.val):
                    currNode.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    currNode.next = ListNode(l2.val)
                    l2 = l2.next
            elif(l1 != None): #when l2 empty
                currNode.next = ListNode(l1.val)
                l1 = l1.next
            elif(l2!= None): #when l1 empty
                currNode.next = ListNode(l2.val)
                l2 = l2.next
            currNode = currNode.next

        return res.next