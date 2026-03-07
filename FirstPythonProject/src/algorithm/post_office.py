from typing import List
from collections import defaultdict, deque
from enum import IntEnum
class PostOffice:
    def get_post_office_position(self, grid: List[List[int]]):
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        adj_list, candidates, house_count = self.build_graph(grid)
        for start in candidates:
            self.bfs(start, grid, adj_list, candidates)

    def bfs(self, pos: tuple[int, int], grid: List[List[int]], adj_list: dict[tuple, list], candidates: set[tuple], house_count: int) -> int:       
        h_count = 0
        total_distance = 0

        queue = deque()
        queue.append(pos)
        distance_to_start = {pos: 0}
        while queue:
            vertex = queue.popleft()
            distance = distance_to_start[vertex]
            for target_ver  in adj_list[vertex]:
                if distance_to_start.get(target_ver, sys.maxsize) > (distance + 1):                 
                    if grid[target_ver[0]][target_ver[1]] == 1:
                        if target_ver in distance_to_start:
                            total_distance += (distance + 1 - distance_to_start[target_ver])
                        else:
                            h_count += 1
                            if h_count == house_count:
                                return total_distance
                            total_distance += (distance + 1)

                    queue.append(target_ver)
                    distance_to_start[target_ver] = distance + 1
                else:
                    continue

        return total_distance


 

    def build_graph(grid: List[List[int]]) -> tuple[dict[tuple, list], set[tuple], int]:
        rows = len(grid)
        cols = len(grid[0])
        adjacency_List = defaultdict(list)

        def try_add_edge(row: int, col: int,):
            rows = len(grid)
            cols = len(grid[0])
            direction = {(-1,0), (0,1), (1,0),(-1,0)}
            for pair in direction:
                if  (0 <= row + pair[0] and  row + pair[0] < rows and 
                     0 <= col + pair[1] and  col + pair[1] < cols and grid[row + pair[0]][col+ pair[1]] != 2):
                    adjacency_List[(row, col)].append((row + pair[0],col+ pair[1]))
    
        house_count = 0
        candidates = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 or grid[row][col] == 1:
                    if grid[row][col] == 0:
                        candidates.add((row, col))
                    else:
                        house_count += 1
                    try_add_edge(row, col, grid, adjacency_List)

        return (adjacency_List, candidates, house_count)



    def bfs_template(self, pos: tuple[int, int], adj_list: list[list]):
        queue = deque(pos)

        while queue:
            node = queue.popleft() 
            
            for move in ((-1, 0),(0, 1),(1, 0),(0, -1)):
                next_pos =(node[0] + move[0], node[1] + move[1])


    def check_valid(self, row, col, grid: list[list]):
        rows, cols = len(grid), len(grid[0])
        if (0 <= row and row < rows and 
            0 <= col and col < cols and grid[row][col] in (GridType.EMPTY, GridType.HOUSE)):
            return True
        return False

class GridType(IntEnum):
    EMPTY = 0
    HOUSE = 1
    WALL = 2