from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class MaxBinaryTree:
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        records = []
        for i in range(len(nums)):
            last_pop_node = None
            new_node = TreeNode(nums[i])

            while records and nums[i] >= records[-1].val:
                current_node = records.pop()
                current_node.right = last_pop_node
                last_pop_node = current_node


            if last_pop_node != None:
                new_node.left = last_pop_node

            if records:
                records[-1].right = new_node
                    
            records.append(new_node)

        return records[0]

            