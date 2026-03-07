from collections import deque
from enum import IntEnum
import heapq

class GridType(IntEnum):
    EMPTY = 0
    WALL = 1


class MazeIII:
    def maze_iii(
        self, grid: list[list], ball: tuple[int, int], hole: tuple[int, int]
    ) -> tuple[int, str]:
        if not grid or not grid[0]:
            return (-1, "impossible")
        if ball == hole:
            return (0, "")
        
        distance_to_start = self.bfs_fix_opt(grid, ball, hole)
        return distance_to_start.get(hole, (-1, "impossible"))


    ## error !!! 第一次找打不一定是最短，因为它不一步一步走的 bfs 而是一脚走的距离，可能第一次找到hole是远，
    ## 对于一次走好几步或者是带权重路，在队列中靠前不能说明任何问题
    ## 但是一次一步或边的权重一，，则能体现在队列中考前 需要步数少 距离短
    def bfs(
        self, grid: list[list], ball: tuple[int, int], hole: tuple[int, int]
    ) -> tuple[int, str]:
        queue = deque((ball[0], ball[1], None))
        distance_to_start = {ball: 0}
        while queue:
            pos = queue.popleft()

            for move in ((-1, 0, "d"), (0, 1, "r"), (1, 0, "u"), (1, 0, "u")):
                next_pos = pos[0] + move[0], pos[1] + move[1]
                if (
                    next_pos in distance_to_start
                    and distance_to_start[next_pos] < distance_to_start[pos] + 1
                ) or not self.check_vaild(next_pos, grid):
                    continue

                while (
                    next_pos not in distance_to_start
                    or distance_to_start[next_pos] > distance_to_start[pos] + 1
                ) and self.check_vaild(next_pos, grid):
                    if pos == hole:
                        path = []
                        for i in range(1, len(queue), 1):
                            path.append(queue[i][2])
                        path.append(move[2])
                        return distance_to_start[pos], "".join(path)

                    distance_to_start[next_pos] = distance_to_start[pos] + 1
                    last_vaild_pos = next_pos
                    next_pos = pos[0] + move[0], pos[1] + move[1]

                queue.append((last_vaild_pos[0], last_vaild_pos[1], move[2]))

        return (-1, "impossible")

    def bfs_fix(
        self, grid: list[list], ball: tuple[int, int], hole: tuple[int, int]) -> dict[tuple[int, int], tuple[int, str]]:
        queue = deque([ball])
        distance_to_start = {ball: (0, "")}
        while queue:
            pos = queue.popleft()

            #note down => row + 1
            for move in ((-1, 0, "u"), (0, 1, "r"), (1, 0, "d"), (0, -1, "l")):

                next_pos = pos[0] + move[0], pos[1] + move[1]
                last_vaild_pos = None
                length = 0
                # stop: hole or wall 
                while (self.check_vaild(next_pos, grid)):  
                    length += 1  
                    last_vaild_pos = next_pos
                    if next_pos == hole:
                        break
                    next_pos = next_pos[0] + move[0], next_pos[1] + move[1]

                if (last_vaild_pos is None or
                    last_vaild_pos in distance_to_start
                    and distance_to_start[last_vaild_pos][0] <= distance_to_start[pos][0] + length
                ) or not self.check_vaild(last_vaild_pos, grid):
                    continue

                if next_pos != hole:
                    queue.append((last_vaild_pos[0], last_vaild_pos[1]))
                distance_to_start[last_vaild_pos] = (distance_to_start[pos][0] + length, distance_to_start[pos][1] + move[2])
        return distance_to_start


    def bfs_fix_opt(
        self, grid: list[list], ball: tuple[int, int], hole: tuple[int, int]) -> dict[tuple[int, int], tuple[int, str]]:
        pq = []
        heapq.heappush(pq, (0, ball))
        distance_to_start = {ball: (0, "")}
        while pq:
            dist, pos = heapq.heappop(pq)
            _, path = distance_to_start[pos]

            #note down => row + 1
            for move in ((-1, 0, "u"), (0, 1, "r"), (1, 0, "d"), (0, -1, "l")):
                if path and path[-1] == move[2]:
                    continue
                next_pos = pos[0] + move[0], pos[1] + move[1]
                last_vaild_pos = None
                length = 0
                # stop: hole or wall 
                while (self.check_vaild(next_pos, grid)):    
                    length += 1
                    last_vaild_pos = next_pos
                    if next_pos == hole:
                        break
                    
                    next_pos = next_pos[0] + move[0], next_pos[1] + move[1]
                if last_vaild_pos is None:
                    continue
                if (last_vaild_pos in distance_to_start and 
                    ((distance_to_start[last_vaild_pos][0] < distance_to_start[pos][0] + length) or
                      (distance_to_start[last_vaild_pos][0] == distance_to_start[pos][0] + length and 
                       distance_to_start[last_vaild_pos][1] <= distance_to_start[pos][1] + move[2]))):
                    continue

                distance_to_start[last_vaild_pos] = (distance_to_start[pos][0] + length, distance_to_start[pos][1] + move[2])
                if next_pos != hole:
                    heapq.heappush(pq, (distance_to_start[last_vaild_pos][0], last_vaild_pos))
        return distance_to_start

    def check_vaild(self, pos: tuple[int, int], grid: list[list]) -> bool:
        rows, cols = len(grid), len(grid[0])
        if (
            0 <= pos[0]
            and pos[0] < rows
            and 0 <= pos[1]
            and pos[1] < cols
            and grid[pos[0]][pos[1]] == GridType.EMPTY
        ):
            return True
        return False

if __name__ == "__main__":
    s = MazeIII()

    # LeetCode 499 Example 1: expect dist=6, path="lul"
    grid1 = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
    ]
    r = s.maze_iii(grid1, (4, 3), (0, 1))
    print(f"Test 1: {r}  expect (6, 'lul')")
    assert r == (6, "lul"), f"FAIL: {r}"

    # Impossible
    grid2 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    r = s.maze_iii(grid2, (0, 0), (2, 2))
    print(f"Test 2: {r}  expect (-1, 'impossible')")
    assert r == (-1, "impossible"), f"FAIL: {r}"

    # Ball == hole
    r = s.maze_iii([[0]], (0, 0), (0, 0))
    print(f"Test 3: {r}  expect (0, '')")
    assert r == (0, ""), f"FAIL: {r}"

    # Direct roll
    r = s.maze_iii([[0, 0, 0, 0, 0]], (0, 0), (0, 3))
    print(f"Test 4: {r}  expect (3, 'r')")
    assert r == (3, "r"), f"FAIL: {r}"

    print("All tests passed!")