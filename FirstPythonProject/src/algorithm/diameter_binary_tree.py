from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DiameterOfBinaryTree:
    diameter = 0
    def diameter_binary_tree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        DiameterOfBinaryTree.diameter = 0
        
        self.dfs(root)
        return DiameterOfBinaryTree.diameter

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 0
        left_deep, right_deep = 0 , 0 
        if root.left != None:
            left_deep = self.dfs(root.left) + 1

        if root.right != None:
            right_deep = self.dfs(root.right) + 1
        if DiameterOfBinaryTree.diameter < left_deep  + right_deep:
            DiameterOfBinaryTree.diameter = left_deep  + right_deep
        return max(left_deep, right_deep)
    
    def dfs_non_recursive(self, root: Optional[TreeNode], stack) -> int:
        if root.left == None and root.right == None:
            return 0
        
        node = root
        left_deep = 0
        while node != None or stack:
            if node != None:        
                stack.append(node)
                #visit root
                if node.left == None:
                    left_deep = 0
                node = node.left
            else:
                node = stack.pop()
                if node.right== None:
                    right_deep = 0
                node = node.right

    def diameter_binary_tree_nested_function(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        diameter = 0

        def dfs(root):
            nonlocal diameter
            if root.left == None and root.right == None:
                return 0
            left_deep, right_deep = 0 , 0 
            if root.left != None: 
                left_deep = dfs(root.left) + 1

            if root.right != None:
                right_deep = dfs(root.right) + 1
            if diameter < left_deep  + right_deep:
                diameter = left_deep  + right_deep
            return max(left_deep, right_deep)
        dfs(root)
        return diameter
