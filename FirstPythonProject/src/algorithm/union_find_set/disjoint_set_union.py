class UnionFindSet:
    def __init__(self):
        self.father = {}
        
    def add(self, x):
        if x in self.father:
            return 
        self.father[x] = x

    # 路径压缩 找一次父亲 后将路径上所有节点都指向了 root
    # 减少 路径高度  
    def find(self, x): 
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, x, y):
        x_root  = self.find(x)
        y_root  = self.find(y)
        self.father[y_root] = x_root