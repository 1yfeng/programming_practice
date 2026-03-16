from typing import List

class FindMaxXOR:
    # try array - list

    def find_maximum_xor_list(self, nums: List[int]) -> int: 
        if not nums:
            return 0

        trie = self.build_trie_by_list(nums)
        n = len(nums)
        max = 0
        for i in range(n):
            target_num = self.get_best_pair(nums, nums[i])
            result = nums[i] ^ target_num
            if max < result:
                max = result
        return max  

    def build_trie_by_list(self, nums: List[int]) -> list[list[int]]:
        NUM_BITS = 32
        n = len(nums)
        #note 
        trie_store = [[0 for _ in range(2)] for _ in range(NUM_BITS * (n + 1))]
        node_count = 0
        root = trie_store[0]
        for i in range(n):
            node = root
            num = nums[i]
            for j in range(NUM_BITS - 1, -1, -1):
                bit = num >> j  & 1
                if node[bit] == 0:
                    node_count += 1
                    node[bit] = node_count
                    node = trie_store[node_count]
                else:
                    node = trie_store[node[bit]]
        return trie_store

    def get_best_pair(self, trie: list[list[int]], num: int) -> int:
        node = trie[0]
        result = 0
        for i in range(31, -1, -1):
            bit = num >> i & 1
            find_bit =  1 - bit
            if node[find_bit] != 0:
                result += find_bit << i
                node = trie[node[find_bit]]      
            else:
                result += bit << i
                node = trie[node[bit]]
             

        return result 
