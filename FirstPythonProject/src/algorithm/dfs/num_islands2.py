from typing import List
from collections import deque

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class NumIslands2:
    def num_island2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        if not operators:
            return []

        k = len(operators)
        result = [1] * k
        map = [[0 for _ in range(m)] for _ in range(n)]       
        self.set_and_check(map, operators[0])
        for i in range(1, k):
            result[i] = result[i-1] + self.set_and_check(map, operators[i])
                

        return result


    def set_and_check(self, map: list[list[int]], pos: Point) -> int:
        if map[pos.x][pos.y] == 1:
            return 0
        else:
            map[pos.x][pos.y] = 1
            rows, cols = len(map), len(map[0])
            connect_set_list = []
            for neibor in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                next_x, next_y = pos.x + neibor[0], pos.y + neibor[1]
                has_connected = False
                #print(next_x, next_y, map[next_x][next_y] )
                if (0<= next_x and next_x < rows and
                    0 <= next_y and next_y < cols and map[next_x][next_y] == 1):       
                    for c_set in connect_set_list:
                        if (next_x, next_y) in c_set:
                            has_connected = True
                            break
                    if not has_connected:
                        connect_set_list.append(self.bfs(map, next_x, next_y))

            return 1 - len(connect_set_list)


    def bfs(self, map: list[list[int]], start_x: int, start_y: int) -> set:
        queue = deque([(start_x, start_y)])
        connect_set =set([(start_x, start_y)])
        rows, cols = len(map), len(map[0])
        while queue:
            pos = queue.popleft()
            for nove in ((-1, 0),(0, 1),(1, 0),(0, -1)):
                next_x, next_y = pos[0] + nove[0], pos[1] + nove[1]
                #print(next_x, next_y, map[next_x][next_y] )
                if (0<= next_x and next_x < rows and
                    0 <= next_y and next_y < cols and map[next_x][next_y] == 1):
                    queue.append((next_x, next_y))
                    connect_set.add((next_x, next_y))

        