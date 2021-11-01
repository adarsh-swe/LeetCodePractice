"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodes = { None : None }

        temp = head
        while(temp != None):
            newNode = Node(temp.val)
            nodes[temp] = newNode
            temp = temp.next 

        temp = head 
        while(temp != None):

            newNode = nodes[temp]
            newNode.next = nodes[temp.next]
            newNode.random = nodes[temp.random]
            temp = temp.next
        
        return nodes[head]