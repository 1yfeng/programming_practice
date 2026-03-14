from typing import List
from collections import deque
class GenerateParenthesis:
    def generate_parenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return None
        result = []
        path = [""] * (2 * n)
        def dfs(n: int, l_p: int , r_p: int, path: list[str]) -> list[str]:
            nonlocal result
            if 2*n == (l_p + r_p):
                result.append("".join(path))
                return 
            
            if l_p < n:
                path[l_p + r_p] = '('
                dfs(n, l_p + 1, r_p, path)
            if r_p < n and l_p > r_p:
                path[l_p + r_p] = ')'
                dfs(n, l_p, r_p + 1, path)
            return                 
        dfs(n, 0, 0, path )
        return result
        
    def generate_parenthesis_iteration(self, n: int) -> List[str]:
        if n <= 0:
            return None
        result = []
        path = []
        last_traversal = None
        last_traversal_deep = 0
        l_p  = 0
        r_p  = 0
        while path or last_traversal_deep > 0:
            if  len(path) == 2 * n:
                result.append("".join(path))
                path.pop()

            # push
            elif (last_traversal_deep < ):



        return result 