# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = [1]
        def dfs(v, max_val, cnt):
            if not v:
                return
            if v.val >= max_val:
                cnt[0] += 1
                max_val = v.val
            dfs(v.left, max_val, cnt)
            dfs(v.right, max_val, cnt)
            return
        
        dfs(root.left, root.val, cnt)
        dfs(root.right, root.val, cnt)
        return cnt[0]

            
            