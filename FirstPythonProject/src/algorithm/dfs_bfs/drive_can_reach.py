from collections import deque
from typing import List
import math
class DriveCanReach:
    def can_reach(self, L :int , D: int, stations: List[List[int]]) -> bool:
        if not stations:
            return (D - abs(L) >= 0)
        if L <= D:
            return True
        target_station = set([])
        n = len(stations)
        for i in range(n):
            if (self.distance(stations[i][0], stations[i][1], L, 0) < D):
                target_station.add((stations[i][0], stations[i][1]))

        print(target_station)
        sorted_x_indexs = sorted(range(n), key = lambda i : stations[i][0])
        sorted_y_indexs = sorted(range(n), key = lambda i : stations[i][1])
        print(sorted_x_indexs, sorted_y_indexs)
        return self.bfs(D,0, 0, sorted_x_indexs, sorted_y_indexs, stations, target_station )

    def bfs(self, D: int, pos_x: int, pos_y: int, 
                            sorted_x_indexs: list[int],
                            sorted_y_indexs: list[int], stations: list[list[int]], target_stations:set) -> bool:
        queue = deque([(pos_x, pos_y)])
        visited = set([(pos_x, pos_y)])

        while queue:
            node = queue.popleft()
            for i in self.get_can_reach_nodes(D, node[0], node[1], sorted_x_indexs, sorted_y_indexs, stations):
                if (stations[i][0], stations[i][1])  not in visited:
                    if (stations[i][0], stations[i][1]) in target_stations:
                        return True
                    queue.append((stations[i][0], stations[i][1]))
                    visited.add((stations[i][0], stations[i][1]))

        return False


    def get_can_reach_nodes(self, D: int, pos_x: int, pos_y: int, 
                            sorted_x_indexs: list[int],
                            sorted_y_indexs: list[int], stations: list[list[int]]) -> set[int]:
        result = set([])
        x_start = self.binary_search_index(pos_x, stations, 0, sorted_x_indexs)
        y_start = self.binary_search_index(pos_y, stations, 1, sorted_y_indexs)

        index = x_start
        n = len(sorted_x_indexs)
        print("sorted_x_indexs[index], index")
        while index < n and self.distance(pos_x, pos_y, stations[sorted_x_indexs[index]][0], stations[sorted_x_indexs[index]][1]) <= D:
            result.add(sorted_x_indexs[index])
            index  += 1 

        index = y_start
        while index < n and self.distance(pos_x, pos_y, stations[sorted_y_indexs[index]][0], stations[sorted_y_indexs[index]][1]) <= D:
            result.add(sorted_y_indexs[index])
            index  += 1 

        print(f"result = {result},x_start = {x_start},y_start = {y_start}")
        return result
        

    
    def distance(self, x1: int, y1: int, x2: int, y2: int):
        return math.sqrt((x1- x2)** 2 + (y1 - y2)** 2)


    def binary_search_index(self, target: int, raw_list: list[list[int]], index: int, sorted_indexs: list[int]) -> int:
        vaild_index = 0

        start = 0
        end = len(sorted_indexs)

        while start <= end:
            mid = start + (end - start ) // 2
            if raw_list[sorted_indexs[mid]][index]  < target:
                start =  mid + 1       
            else:
                end = mid - 1
                vaild_index = mid

        return vaild_index
            
if __name__ == "__main__":
    d = DriveCanReach()
    #print(d.can_reach(10, 5, [[4,0], [7,0]]))
    print(d.can_reach(10, 4, [[5,5]]))
