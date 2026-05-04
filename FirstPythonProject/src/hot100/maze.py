from typing import List
from collections import deque
class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    map = {0:2, 1:3, 2:0, 3: 1}
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0]:
            return False

        return self.bfs(maze, start, destination)

    def bfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start[0]==destination[0] and  start[1]== destination[1]:
            return True
        queue = deque([(start[0], start[1])])
        visited = set([(start[0], start[1])])
        dircet =Solution.directions
        # map =Solution.map
        n = len(dircet)
        row, col = len(maze),len(maze[0]) 
        while queue:
            cur_pos = queue.popleft()
            for i in range(n):
                next_pos = (cur_pos[0], cur_pos[1])
                while (0 <= (next_pos[1] + dircet[i][1]) < col and 
                       0 <= (next_pos[0] + dircet[i][0]) < row  and 
                       maze[next_pos[0] + dircet[i][0] ][next_pos[1] + dircet[i][1]] == 0):
                    next_pos = (next_pos[0] + dircet[i][0], next_pos[1] + dircet[i][1])
                if next_pos[0]==destination[0] and  next_pos[1]== destination[1]:
                    return True

                record = (next_pos[0], next_pos[1]) 
                if record not in visited:
                    queue.append(record)
                    visited.add(record)
                
        
        return False
                