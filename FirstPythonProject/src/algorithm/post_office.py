from typing import List
from collections import defaultdict
class PostOffice:
    def get_post_office_position(self, grid: List[List[int]]):
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        






    def build_graph(grid: List[List[int]], ) -> dict[tuple, list]:
        rows = len(grid)
        cols = len(grid[0])
        adjancy_List = defaultdict(list)

        def try_add_edge(row: int, col: int,):
            rows = len(grid)
            cols = len(grid[0])
            direction = {(-1,0), (0,1), (1,0),(-1,0)}
            for pair in direction:
                if  (0 <= row + pair[0] and  row + pair[0] < rows and 
                     0 <= col + pair[1] and  col + pair[1] < cols and grid[row + pair[0]][col+ pair[1]] != 2):
                    adjancy_List[(row, col)].append((row + pair[0],col+ pair[1]))

                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 2:
                    try_add_edge(row, col, grid, adjancy_List)


                    

        return adjancy_List



