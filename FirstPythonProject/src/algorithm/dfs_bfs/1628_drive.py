from typing import List
from collections import defaultdict, deque
import math
class Drive1628:
    car_radius = 2
    barrier_radius = 1
    def can_reach(self, L: int, W : int, barriers: List[List[int]]) -> str:
        if not barriers:
            return (2 * Drive1628.car_radius) <= W
        n = len(barriers)
        adj_list = self.build_graph(barriers, W)
        visited = set([])
        for i in range(n):
            if (barriers[i][0], barriers[i][1]) not in visited:
                if self.bfs(barriers, barriers[i], visited, adj_list, W):
                    return "no"
                
        return "yes"

    def bfs(self, barriers:list[list[int]], 
            start_node: list[int], visited: set, adj_list: dict, W: int) -> bool:
        queue = deque([(start_node[0], start_node[1])])
        visited.add((start_node[0], start_node[1]))

        connect_top = False
        connect_bottom =False
        while queue:
            node = queue.popleft()
            if node[1] == 0:
                connect_bottom = True
            if node[1] == W:
                connect_top = True
            for next_node in adj_list[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
        return connect_bottom and connect_top        
    
    def build_graph(self, barriers: List[List[int]], W: int) -> dict:
        adj_list = defaultdict(list)

        n = len(barriers)
        barriers_limit = Drive1628.car_radius * 2 + Drive1628.barrier_radius * 2
        for i in range(n):
            if (barriers[i][1] < (Drive1628.car_radius * 2 + Drive1628.barrier_radius)):
                adj_list[(barriers[i][0], barriers[i][1])].append((barriers[i][0], 0))
                adj_list[(barriers[i][0], 0) ].append((barriers[i][0], barriers[i][1]))
            if (barriers[i][1] > (W - Drive1628.car_radius * 2 - Drive1628.barrier_radius)):
                adj_list[(barriers[i][0], barriers[i][1])].append((barriers[i][0], W))
                adj_list[(barriers[i][0], W) ].append((barriers[i][0], barriers[i][1]))

            for j in range(n):
                if j == i:
                    continue
                if abs(barriers[i][0] - barriers[j][0]) > barriers_limit:
                    continue
                if abs(barriers[i][1] - barriers[j][1]) > barriers_limit:
                    continue
                if (math.sqrt(
                    (barriers[i][0] - barriers[j][0])**2 +
                    (barriers[i][1] - barriers[j][1])**2
                ) > barriers_limit):
                    continue
                else:
                    adj_list[(barriers[i][0], barriers[i][1])].append((barriers[j][0], barriers[j][1]))
                    adj_list[(barriers[j][0], barriers[j][1])].append((barriers[i][0], barriers[i][1]))
        return adj_list

if __name__ == "__main__":
    d = Drive1628()
    print(d.can_reach(8, 8, [[1, 1],[6,6]]))