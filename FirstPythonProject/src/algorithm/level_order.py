# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque

class level_order:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [root]
        
        return self.bfs(root)

    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = [[root.val]]

        while queue:
            n = len(queue)
            level_list = []
            for i in range(n):
                node = queue.popleft()
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            result.append(level_list)

        return result
                
            
                 