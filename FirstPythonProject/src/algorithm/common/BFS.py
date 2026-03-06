from typing import List
from collections import deque

class BFS:
    def template(self, data: List[List[str]]):
        
        rows, cols = len(data), len(data[0])
        queue = deque()
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        x, y = 0, 0
        
        queue.append((x, y))
        visited[0][0] = True

        while queue:
            now = queue.popleft()
            for next_point in self.find_next(now):
                if not self.is_valid(now):
                    continue
                if data[now[0]][now[1]] == "1":
                    queue.append(next_point)
                visited[next_point[0]][next_point[1]] = True

    
    def find_next(self, now: tuple[int, int]) -> List:
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = []
        for pair in move:
            x, y = now[0] + pair[0], now[1] + pair[1] 
            result.append((x, y))
        return result
    
    def is_valid(self, now: tuple[int, int], visited: list[list[bool]]) -> List:
        rows, cols = len(visited), len(visited[0]) 
        if  (0 <= now[0] and now[0] < rows and 
                0 <= now[1] and now[1] < cols and not visited[now[0]][now[1]]):
            return True
        return False




    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        count = 0

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col]:
                    if grid[row][col] == "1":
                        self.bfs_visit(grid, visited, row, col, queue)
                        count += 1
                        self.search(grid, visited, queue)
                    else:
                        visited[row][col] = True
        return count

    def bfs(self, row: int, col: int, visited):
        queue  = deque()

        # add visit row col ; while ; 
        self.search()



    def search(self, grid: List[List[str]], visited: list[list[bool]], queue):
        while queue:
            (row, col) = queue.popleft()
            self.bfs_visit(grid, visited, row, col, queue)
    
    def bfs_visit(self,grid: List[List[str]], visited: list[list[bool]], 
                  row: int, col: int, queue) -> int:
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = len(visited), len(visited[0]) 

        for pair in move:
            x, y = row + pair[0], col + pair[1]
            if  (0 <= x and x < rows and 
                 0 <= y and y < cols and not visited[x][y]):
                visited[x][y] = True
                if grid[x][y] == "1":
                    queue.append((x, y))
