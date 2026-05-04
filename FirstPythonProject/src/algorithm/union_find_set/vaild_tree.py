from typing import List
from collections import deque
class VaildTree:
    def vaild_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n > 1:
                return False
            return True 
        #adjacency list
        adj_list = self.build_graph(n, edges)
        return self.bfs(0, adj_list)

    def bfs(self, start: int , adj_list: list[list[int]]) -> bool:
        queue = deque([(start, start)])
        visited = set([start])
        while queue:
            node  = queue.popleft()
            for target_node  in adj_list[node[0]]:
                if target_node == node[1]:
                    continue
                if target_node in visited:
                    return False
                queue.append((target_node, node[0]))
                visited.add(target_node)
        if len(adj_list) != len(visited):
            return False
        
        return True

    def build_graph(self, n: int,  edges: List[List[int]]) -> list[list[int]]:
        adj_list = [[] for _ in range(n)]

        for edge in edges:
            # todo: support multiple same edges 
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list
