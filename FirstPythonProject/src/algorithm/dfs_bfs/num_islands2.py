from typing import List
from collections import deque, defaultdict

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
            for neighbor in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                next_x, next_y = pos.x + neighbor[0], pos.y + neighbor[1]
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
            for nove in ((-1, 0),(0, 1),(1, 0),(0, -1), (0,0 )):
                next_x, next_y = pos[0] + nove[0], pos[1] + nove[1]
                #print(next_x, next_y, map[next_x][next_y] )
                if (0<= next_x and next_x < rows and
                    0 <= next_y and next_y < cols and map[next_x][next_y] == 1):
                    queue.append((next_x, next_y))
                    connect_set.add((next_x, next_y))

    def num_island2_try2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        if not operators:
            return []

        k = len(operators)
        result = [1] * k
        map = [[0 for _ in range(m)] for _ in range(n)]
        group_num = 0
        point_to_group = defaultdict(int)
        group_to_points = defaultdict(list)
        empty_group_ids = set()

        for i in range(k):
            group_num = self.process(map, point_to_group, group_to_points, empty_group_ids, operators[i], group_num)
            result[i] = group_num
                

        return result
    
    def process(self, map: dict, point_to_group: dict, group_to_points: dict, empty_group_ids: set,  pos: Point, group_num: int) -> int:
        if map[pos.x][pos.y] == 1:
            return group_num
        map[pos.x][pos.y] = 1
        if group_num == 0:
            group_num += 1
            pos_tuple = (pos.x, pos.y)
            point_to_group[pos_tuple] = group_num
            group_to_points[group_num].append(pos_tuple)
            return group_num
        
        rows, cols = len(map), len(map[0])
        groups = set()
        for move in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            next_x, next_y = pos.x + move[0], pos.y + move[1]
            if (0<= next_x and next_x < rows and
                0 <= next_y and next_y < cols and map[next_x][next_y] == 1):
                groups.add(point_to_group[(next_x, next_y)])
        group_num = 1 + group_num - len(groups) 
        if groups and len(groups) >= 1:
            self.merge(point_to_group, group_to_points, groups, empty_group_ids, pos)
        else:
            if empty_group_ids:
                group_id = empty_group_ids.pop()
            else:
                group_id = group_num
            group_to_points[group_id].append((pos.x, pos.y))
            point_to_group[(pos.x, pos.y)] = group_id
        
        return group_num
        
    def merge(self, point_to_group: dict, group_to_points: dict, merge_groups: set, empty_group_ids: set, point: Point):
        target = None
        for group in merge_groups:
            if not target:
                    target = group
                    continue
            group_list = group_to_points[group]
            group_to_points[target].extend(group_list)
            group_to_points[group] = []
            for p in group_list:
                point_to_group[p] = target

            empty_group_ids.add(group)
        group_to_points[target].append((point.x, point.y))
        point_to_group[(point.x, point.y)] = target

