class KnightPprobability:
    def knight_probability(self, n: int, k: int, r: int, c: int) -> float:
        if k <= 0:
            return (0 <= r and r <= n - 1) and (0 <= c and c <= n - 1)

        dp = [[[0] * n for _ in range(n)] for _ in range(k)]

        for pos in self.get_on_chessboard((r, c), n):
            dp[0][pos[0]][pos[1]] = 1 / 8
        
        for k_i in range(1, k):
            for i in range(n):
                for j in range(n):
                    for pos in self.get_on_chessboard((i, j), n):
                        dp[k_i][i][j] = dp[k_i][i][j] + dp[k_i - 1][pos[0]][pos[1]] / 8

        result = 0
        for i in range(n):
            for j in range(n):
                result += dp[k -1][i][j]
        return  result

    def knight_probability_opt_storage(self, n: int, k: int, r: int, c: int) -> float:
        if k <= 0:
            return (0 <= r and r <= n - 1) and (0 <= c and c <= n - 1)

        dp = [[[0] * n for _ in range(n)] for _ in range(2)]


        for pos in self.get_on_chessboard((r, c), n):
            dp[1][pos[0]][pos[1]] = 1 / 8
        
        new = 1
        old = 0
        for k_i in range(1, k):
            new = 1 - new
            old = 1 - old
            for i in range(n):
                for j in range(n):
                    dp[new][i][j] = 0 
                    for pos in self.get_on_chessboard((i, j), n):
                        dp[new][i][j] = dp[new][i][j] + dp[old][pos[0]][pos[1]] / 8

        result = 0
        for i in range(n):
            for j in range(n):
                result += dp[k%2][i][j]
        return  result


    def get_on_chessboard(self, pos: tuple[int, int], n: int) -> list[tuple[int, int]]:
        result = []
        for move in [
                [1, 2],
                [2, 1],
                [2, -1],    
                [1, -2],
                [-1, -2],
                [-2, -1],
                [-2, 1],
                [-1, 2],
            ]:
            pos_next = (pos[0] + move[0], pos[1] + move[1])
            if ((0 <= pos_next[0] and pos_next[0] < n) and
                (0 <= pos_next[1] and pos_next[1] < n)):
                result.append(pos_next)
        return result

    
    def move_next(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        return [
            (pos[0] + move[0], pos[1] + move[1])
            for move in [
                [1, 2],
                [2, 1],
                [2, -1],
                [1, -2],
                [-1, -2],
                [-2, -1],
                [-2, 1],
                [-1, 2],
            ]
        ]
    
    def filter_on_chessboard(self, next_pos_list: list[tuple[int, int]], n: int) -> list[tuple[int, int]]:
        result = []
        for pos in next_pos_list:
            if ((0 <= pos[0] and pos[0] < n) and
                (0 <= pos[1] and pos[1] < n)):
                result.append(pos)
        return result
    

if __name__ == "__main__":
    s = "sadasd dasd asd"
    print(s.split(" "))