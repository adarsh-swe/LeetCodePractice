# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node,max,min):
            if(node == None):
                return True
            elif(min != None and min >= node.val) or (max != None and max <= node.val):
                return False
            else:
                return check(node.left,node.val,min) and check(node.right,max,node.val)
        
        res = check(root,None,None)
        return res