from typing import List
from collections import defaultdict, deque

""" 
try again, second coding 
frist no ideas
"""

class TreeLongestPath2:
    def tree_longest_path(self, n: int, starts: List[int], ends: List[int], lens: List[int]) -> int:
        if not starts or not ends or not lens:
            return -1
        
        head_nodes = defaultdict(list)
        n = len(starts)
        for i in range(n):
            start_targets = head_nodes[starts[i]]
            start_targets.append((ends[i], lens[i]))

            end_targets = head_nodes[ends[i]]
            end_targets.append((starts[i], lens[i]))
            
        # max_chain, longest_path =  self.dfs(starts[0], head_nodes, -1)
        max_start, _ = self.bfs(starts[0], head_nodes)
        max_end, longest_path = self.bfs(max_start, head_nodes)
        return longest_path
    
    def dfs(self, node: int, head_nodes: dict[int, list], from_node: int) -> tuple[int, int]:
        n = len(head_nodes[node])
        if n == 1 and head_nodes[node][0][0] == from_node:
            return  0, 0
        
        first_max_chain= 0
        second_max_chain = 0
        longest_path = 0
        
        for child, dist in head_nodes[node]:
            if child == from_node:
                continue
            max_chain, chaild_longest_path =  self.dfs(child, head_nodes, node)
            max_chain += dist
            if  first_max_chain < max_chain:
                if first_max_chain != 0:
                    second_max_chain = first_max_chain
                first_max_chain = max_chain
            elif second_max_chain < max_chain:
                second_max_chain = max_chain
            longest_path = max(longest_path, chaild_longest_path)
        
        return first_max_chain, max(longest_path, first_max_chain + second_max_chain)

            
    def dfs_error(self, node: int, head_nodes: dict[int, list], from_node: int) -> tuple[int, int]:
        n = len(head_nodes[node])
        if n == 1 and head_nodes[node][0][0] == from_node:
            return  0, 0
        
        first_max_chain= 0
        second_max_chain = 0
        
        for child, dist in head_nodes[node]:
            if child == from_node:
                continue
            max_chain, longest_path =  self.dfs(child, head_nodes, node)
            max_chain += dist
            if  first_max_chain < max_chain:
                if first_max_chain != 0:
                    second_max_chain = first_max_chain
                first_max_chain = max_chain
            elif second_max_chain < max_chain:
                second_max_chain = max_chain
        
        return max_chain, max(longest_path, first_max_chain + second_max_chain)


    def bfs(self, node: int, head_nodes: dict[int, list]) -> tuple[int, int]:
        queue = deque()
        queue_length = deque()

        max_node = node
        max_length = 0
        visited = set()
        queue.append(node)
        queue_length.append(0)
        visited.add(node)

        while queue:
            start = queue.popleft()
            length = queue_length.popleft()
            for end in head_nodes[start]:
                if end[0] in visited:
                    continue
                visited.add(end[0])
                cur_length = length + end[1]
                if cur_length > max_length:
                    max_length = cur_length
                    max_node = end[0]
                queue.append(end[0])
                queue_length.append(cur_length)

        return max_node, max_length
            

    def bfs_2(self, node: int, head_nodes: dict[int, list]) -> tuple[int, int]:
        queue = deque()
        distance_to_root = {}

        max_node = node
        max_length = 0

        queue.append(node)
        distance_to_root[node] = 0

        while queue:
            start = queue.popleft()

            for end in head_nodes[start]:
                if end[0] in distance_to_root:
                    continue
  
                cur_length = distance_to_root[start] + end[1]
                if cur_length > max_length:
                    max_length = cur_length
                    max_node = end[0]
                queue.append(end[0])
                distance_to_root[end[0]] = cur_length

        return max_node, max_length


if __name__ == "__main__":
    t = TreeLongestPath2()   
    print()
    print( t.tree_longest_path(n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[5,2,5,6]))
