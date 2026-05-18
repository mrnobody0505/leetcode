# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(v, min_val, max_val):
            if not v:
                return True
            if not (min_val < v.val and v.val < max_val):
                return False
            return dfs(v.left, min_val, v.val) and dfs(v.right, v.val, max_val)
        
        return dfs(root, float('-inf'), float('inf'))
        