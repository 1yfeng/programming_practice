from typing import List
from collections import defaultdict, deque
import math
import sys
import heapq

class ModernLudo:
    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        if length <= 1:
            return -1
        if not connections:
            return math.ceil((length - 1)/ 6)
        
        records = [sys.maxsize] * (length + 1)

        head_list = defaultdict(list)
        for i in range(len(connections)):
            head_list[connections[i][0]].append((connections[i][1]))
        
        records[1] = 0
        for i in range(1, length + 1, 1):
            if i in head_list:   
                for end in head_list[i]:
                    if records[end] > records[i]:
                        records[end] = records[i]
            
            for j in range(i + 1, min(length + 1, i + 7), 1):
                if records[j] > (records[i] + 1):
                    records[j] = records[i] + 1
        
        return records[length]



class Experiment:
    def __init__(self, name):
        self.name = name

    
    def find_shotest_path(self, length: int, connections: list[list[int]]) -> int:
        if length <= 0:
            return -1
        
        if not connections:
            return math.ceil((length - 1)/ 6)
        
        distance_to_start = {}
        distance_to_start[1] = 0
        adjacency_list = [[] for _ in range(length + 1)]
        for pair in connections:
            adjacency_list[pair[0]].append((pair[1], 0))

        for i in range(1, length + 1, 1):
            for j in range(i + 1, min(i + 7, length + 1), 1):
                adjacency_list[i].append((j, 1))


        return self.bfs(adjacency_list, distance_to_start)

    def bfs(self, adjacency_list: list[list[tuple[int, int]]], distance_to_start: dict[int, int]) -> int:
        queue = deque()
        queue.append(1)

        while queue:
            cur_node = queue.popleft()
            for vertex, length in adjacency_list[cur_node]:
                if distance_to_start.get(vertex, sys.maxsize) > distance_to_start[cur_node] + length:
                    distance_to_start[vertex] = distance_to_start[cur_node] + length
                    queue.append(vertex)

        return distance_to_start[len(adjacency_list) - 1]
    
    def build_graph(self, length: int):
        graph =  {
            i: set()
            for i in range(1, length + 1)
        }



if __name__ == "__main__":
    pq = []
    heapq.heappush(pq, 5)
    heapq.heappush(pq, 4)
    heapq.heappush(pq, 1)
    print("result:", heapq.heappop(pq))

