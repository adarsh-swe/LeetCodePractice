# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # recursive solution: (25% runtime, 14% memory usage)
        # res = []
        # def inOrder(self,node):
        #     if (node is None):
        #         return
        #     if(node.left):  
        #         inOrder(self,node.left)
        #     res.append(node.val)
        #     if(node.right):
        #         inOrder(self,node.right)
        # inOrder(self,root)
        # return res

        # Iterative Approach (%6 runtime, %59 memory usage) 
        res = [] 
        stack = [] 
        temp = root
        while(temp != None or len(stack) != 0):
            while (temp != None):
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            res.append(temp.val)   
            temp = temp.right
        return res 

