from typing import List
from collections import defaultdict,deque


class numSimilarGroups:
    def num_similar_groups(self, strs: List[str]) -> int:
        adj_list = self.build_graph(strs)
        visited = set([])
        count = 0

        for s in strs:
            if s not in visited:
                self.bfs(adj_list, s, visited)
                count += 1

        return count

    def bfs(self, adj_list: dict[str, list],  node: str, visited:set): 
        queue =deque([node])
        visited.add(node)

        while queue:
            node_pop = queue.popleft()
            for neighbor in  adj_list[node_pop]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def check_similar(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2:
            return False
        diff_list = []
        for i in range(n1):
            if s1[i] != s2[i]:
                if len(diff_list) < 2:
                    diff_list.append(i)
                else:
                    return False

        if diff_list:
            if (
                len(diff_list) == 2
                and s1[diff_list[0]] == s2[diff_list[1]]
                and s1[diff_list[1]] == s2[diff_list[0]]
            ):
                return True
            return False
        else:
            return True

    def build_graph(self, strs: List[str]) -> dict[str, list]:
        adj_list = defaultdict(list)
        n = len(strs)
        # todo 总结 矩阵 一半
        # how to write loop best? eg, for j in range(i + 1, n):
        for i in range(n):
            for j in range(i + 1, n):
                if self.check_similar(strs[i], strs[j]):
                    adj_list[strs[i]].append(strs[j])
                    adj_list[strs[j]].append(strs[i])

        return adj_list
