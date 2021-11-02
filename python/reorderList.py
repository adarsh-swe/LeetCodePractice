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
        
        copy = [] #store all nodes 
        temp = head 
        while temp != None:
            copy.append(temp)
            temp = temp.next  
           
        half = len(copy)//2
        first = copy[:half]
        second = copy[half:]
        second.reverse()

        i = 1
        j = 0 

        while(i < len(first) or j<len(second)):
            if(j < len(second)):
                head.next = second[j]
                head = head.next 
                print(head.val)
            if (i < len(first)):
                head.next = first[i]
                head = head.next
                print(head.val)
            
            i+=1 
            j+=1 

        head.next = None
            
# Even length 1->2->3->4
# expected = 1->4->2->3

# Odd length  1->2->3->4->5
# expected = 1->5->2->4->3

# empty set None
# expected = None 