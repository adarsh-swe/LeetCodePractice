# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #root stored at index i=0 
        #left is at 2i+1 
        #right is at 2i+2 
        #parent at i/2-1
        
        res = []
        if(root == None):
            return res 
        q = queue.Queue()
        q.put(root)
        
        while not q.empty() :
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                if(i == size - 1):
                    res.append(curr.val)
                if(curr.left):
                    q.put(curr.left)
                if(curr.right):
                    q.put(curr.right)
      
        return res
    