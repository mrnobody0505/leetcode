"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        visited = {}
        clone_node = Node(node.val)
        visited[node] = clone_node
        q.append(node)
        while q:
            top_node = q.popleft()
            for neighbor in top_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                visited[top_node].neighbors.append(visited[neighbor])
        
        return clone_node



        