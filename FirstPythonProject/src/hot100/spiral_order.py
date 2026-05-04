from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):       # → 向右
                result.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):       # ↓ 向下
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:                        # ← 向左（至少还有一行）
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:                        # ↑ 向上（至少还有一列）
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
