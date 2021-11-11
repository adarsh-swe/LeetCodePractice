# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root1,root2):
            if not root1 and not root2:
                return None
            val1 = 0 if not root1 else root1.val 
            val2 = 0 if not root2 else root2.val 

            copy = TreeNode(val1+val2)
            copy.right = helper(None if not root1 else root1.right, None if not root2 else root2.right)
            copy.left = helper(None if not root1 else root1.left, None if not root2 else root2.left)
            return copy
        
        return helper(root1,root2)