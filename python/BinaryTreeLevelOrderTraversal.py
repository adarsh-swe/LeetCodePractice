# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if(root == None):
            return res
            
        def bfs(node,level):
            if(level == len(res)):
                res.append([])
            
            if(node):
                res[level].append(node.val)
                if(node.left):
                    bfs(node.left,level+1)
                if(node.right):
                    bfs(node.right,level+1)  

        bfs(root, 0)
        return res