from typing import List
from collections import deque
class CanVisitAllRooms:
    def can_visit_all_rooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        n = len(rooms)
        visited = [False] * n
        self.bfs(rooms, 0, visited)
        for i in range(n):
            if not visited[i]:
                return False
        return True

    def bfs(self, rooms: List[List[int]], pos: int, visited: list[bool]):
        queue = deque([pos])
        visited[pos] = True

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if not visited[key]:
                    queue.append(key)
                    visited[key] = True
        
        return 
