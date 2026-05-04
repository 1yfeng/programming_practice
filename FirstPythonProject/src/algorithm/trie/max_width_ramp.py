from typing import List
class TrieNode:
    def __init__(self, val: int, index: int):
        self.val = val
        self.index = index
        self.largest_index = index
        self.child = {}

class MaxWidthRamp:
    def max_width_ramp(self, nums: List[int]) -> int:
        if not nums:
            return 0
        trie = {True:TrieNode(nums[0], 0)}
        node = trie[True]
        n = len(nums)
        for i in range(1, n):
            self.insert_trie(node, nums[i], i)
        
        width = 0
        while node:
            if width < (node.largest_index - node.index):
                width = node.largest_index - node.index
            
            node = node.child.get(False, None)
        return width

    def insert_trie(self, node: TrieNode, val: int, index: int):

        while node.child and (val >= node.val) in node.child:
            #print(f"node.index = {node.index},node.val = {node.val},node.largest_index = {node.largest_index}")
            if val >= node.val:
                node.largest_index = index
                node = node.child[True]
            else:
                node = node.child[False]

        node.child[val >= node.val] = TrieNode(val, index)
        if val >= node.val:
                node.largest_index = index
        #print(f"node.index = {node.index},node.val = {node.val},node.largest_index = {node.largest_index}")

if __name__ == "__main__":
    m = MaxWidthRamp() 
    print(m.max_width_ramp([9,8,1,0,1,9,4,0,4,1]))
