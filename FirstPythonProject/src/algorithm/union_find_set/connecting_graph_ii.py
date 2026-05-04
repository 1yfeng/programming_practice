class ConnectingGraphII:
    def __init__(self, n : int): 
        self.parent = {}
        self.root2size = {}
        for i in range(n):
            self.parent[i] = i
            self.root2size[i] = 1

    def find(self, a: int) -> int:
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


    def connect(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return 

        if self.root2size[root_a] < self.root2size[root_b]:
            root_a, root_b = root_b, root_a

        self.root2size[root_a] =  self.root2size[root_a] + self.root2size[root_b]
        #del  self.root2size[root_b]
        self.root2size.pop(root_b)
        self.parent[root_b] = root_a
    
    def query(self, a: int) -> int:
        root = self.find(a)
        return self.root2size[root]
