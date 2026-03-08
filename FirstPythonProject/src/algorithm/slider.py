from typing import List
from collections import deque


class Slider:
    def sliding_puzzle(self, board: List[List[int]]) -> int:
        if not board or not board[0]:
            return -1

        rows, cols = len(board), len(board[0])
        start = None
        str_list = []
        count = 1
        for row in range(rows):
            for col in range(cols):
                str_list.append(str(count))
                count += 1
                if board[row][col] == 0:
                    start = (row, col)
        str_list[-1] = "0"

        return self.bfs_sliding_puzzle(start, board, "".join(str_list))

    def bfs_sliding_puzzle(
        self, start: tuple[int, int], board: List[List[int]], target: str
    ) -> int:
        record = self.get_record(board)
        if record == target:
            return 0
        records = {record: 0}
        cols = len(board[0])

        queue = deque([(start, record)])

        while queue:
            pos, last_record = queue.popleft() 
            dist = records[last_record]
            for move in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                next_pos = (pos[0] + move[0], pos[1] + move[1])
                if not self.check_vaild(next_pos, board):
                    continue
                record = self.get_record_by_move(last_record, pos, next_pos, cols)
                if record == target:
                    return dist + 1
                if record in records:
                    continue

                records[record] = dist + 1
                queue.append((next_pos, record))

        return -1

    def get_record(self, board: List[List[int]]) -> str:
        rows, _ = len(board), len(board[0])
        row_list = []
        for row in range(rows):
            row_list.append("".join(str(x) for x in board[row]))
        return "".join(row_list)

    def get_record_by_move(self,
        last_record: str, pos: tuple[int, int], next_pos: tuple[int, int], cols: int
    ) -> str:
        pos_index = pos[0] * cols + pos[1]
        next_pos_index = next_pos[0] * cols + next_pos[1]
        if pos_index < next_pos_index:
            return (
                last_record[:pos_index]
                + last_record[next_pos_index]
                + last_record[(pos_index + 1) : next_pos_index]
                + last_record[pos_index]
                + last_record[next_pos_index + 1 :]
            )
        else:
            return (
                last_record[:next_pos_index]
                + last_record[pos_index]
                + last_record[(next_pos_index + 1) : pos_index]
                + last_record[next_pos_index]
                + last_record[pos_index + 1 :]
            )

    def check_vaild(self, pos: tuple[int, int], board: list[list[int]]) -> bool:
        rows, cols = len(board), len(board[0])
        if 0 <= pos[0] and pos[0] < rows and 0 <= pos[1] and pos[1] < cols:
            return True

        return False
