from collections import defaultdict, deque
class Tree:
    def query_relationship(self, x: list[int], y: list[int], a: list[int], b: list[int]):
        n = len(a)
        records = defaultdict(list)
        for i in range(n):
            records[a[i]].append(i)
        tree = self.build_tree(x, y)
        return self.bfs(tree, a, b, 1, records)
    
    def bfs(self, adj_list: dict, a: list, b: list, root: int, records: dict) -> list:
        n = len(a)
        result = [0] * n
        visited = set([root])

        queue = deque([root])
        while queue:
            node = queue.popleft()
            sons = set([])
            check_borther_indexs = []
            for t_node in adj_list[node]:
                if t_node not in visited:
                    if t_node in records:
                        check_borther_indexs = records[t_node]
                    sons.add(t_node)
                    visited.add(t_node)
                    queue.append(t_node)
            if node in records:
                for i in records[node]:
                    if b[i] in sons:
                        result[i] = 2

                print(f"node={node} in records, i = {i}")
            if check_borther_indexs:
                for i in check_borther_indexs:           
                    if b[i] in sons:
                        result[i] = 1
                    print(f"check_borther_index, check_borther_index = {check_borther_indexs}, sons = {sons},b[i] = {b[i]}")
                

        return result


    def build_tree(self, x:list[int], y:list[int]) -> dict:
        adj_list = defaultdict(list)

        for i in range(len(x)):
            adj_list[x[i]].append(y[i])
            adj_list[y[i]].append(x[i])
        return adj_list


if __name__ == "__main__":
     t = Tree()
     #r = t.query_relationship([1, 1], [2, 3], [1,2], [2, 3])
     r = t.query_relationship([1, 1,2], [2, 3, 4], [1,2,1], [2, 3,4])
     print(r)
        

