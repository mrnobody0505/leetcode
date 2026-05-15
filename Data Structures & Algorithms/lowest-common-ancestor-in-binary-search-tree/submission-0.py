# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited = set()
        def dfs(v):
            visited.add(v)
            if v.val == p.val:
                return
            elif v.val > p.val:
                dfs(v.left)
            else:
                dfs(v.right)
        dfs(root)
        def temp(v, mem):
            if v in visited: mem[0] = v
            if v.val == q.val:
                return
            elif v.val > q.val:
                temp(v.left, mem)
            else:
                temp(v.right, mem)
        
        ans = [0]
        temp(root, ans)

        return ans[0]

            
        

        