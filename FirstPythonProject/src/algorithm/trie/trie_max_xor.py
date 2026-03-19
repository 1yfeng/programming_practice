from typing import List
class FindMaximumXOR:
    def find_max_xor_dict(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        trie = self.build_trie_dict(nums)
        max = 0
        for i in range(n):
            target_num = self.find_best_pair(trie, nums[i])
            result = nums[i] ^ target_num
            if max < result:
                max = result
        return max


    def build_trie_dict(self, nums: list[int]) -> dict:
        trie = {}
        
        n = len(nums)
        for i in range(n):
            node = trie
            for j in range(31, -1, -1):
                bit = nums[i] >> j & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        return trie
    
    def find_best_pair(self, trie: dict, num: int) -> int:
        node = trie

        target_num = 0
        for i in range(31, -1, -1):
            bit = num >> i & 1
            target_bit =  1 ^ bit
            if target_bit in node:
                target_num += target_bit << i
                node = node[target_bit]
            else:
                target_num += bit << i
                node = node[bit]
        return  target_num
