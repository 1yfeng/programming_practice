from typing import (
    List,
)


from collections import deque


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class KnightShortestPath:
    def shortest_path(self, grid: List[List[bool]], source: Point, destination: Point) -> int:
        if not grid or not grid[0]:
            return -1
        queue = deque()
        rows, cols = len(grid), len(grid[0]) 
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        return self.bfs(grid, queue, visited, source.x, source.y, destination.x, destination.y)

    
    def bfs(self, grid: List[List[bool]], queue, visited, x: int, y :int, t_x: int, t_y :int) -> int:
        rows, cols = len(grid), len(grid[0]) 
        queue.append((x, y))
        visited[x][y] = True
        deep = 0
        if x==t_x and y == t_y:
            return deep
        
        while queue:
            queue_size = len(queue)
            deep += 1
            for i in range(queue_size):
                pos = queue.popleft()        
                for next_pos in self.get_next(pos[0], pos[1], rows, cols):
                    if self.is_vaild(grid, visited, next_pos[0], next_pos[1]):
                        if next_pos[0]==t_x and next_pos[1] == t_y:
                            return deep
                        queue.append(next_pos)
                        visited[next_pos[0]][next_pos[1]] = True

        return -1
                

    def get_next(self, x: int, y :int,  rows: int, cols: int):
        directions = {(1, 2),
         (1, - 2),
         (- 1, 2),
         (- 1, - 2),
         (2, 1),
         (2, - 1),
         (- 2, 1),
         (- 2, - 1)}
        next_pos = []
        for pos in directions:
            next_pos.append((x + pos[0], y + pos[1]))
        return next_pos
    
    def is_vaild(self, grid: List[List[bool]], visited: list[list[bool]], x: int, y :int ):
        rows, cols = len(visited), len(visited[0])
        if (0 <= x and x < rows and
            0 <= y and y < cols and not visited[x][y] and not grid[x][y]):
            return True
        return False
