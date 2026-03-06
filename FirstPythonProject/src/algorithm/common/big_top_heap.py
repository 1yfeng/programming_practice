class BigTopHeap:
    def __init__(self, heap = [None], capacity = 0):
        if heap and (heap[0] == None):
            self.heap = heap
        else:
            self.heap = [None, *heap]
        self.capacity = len(self.heap) - 1

    def heapfy(self, index: int, heap_size: int):
        while index * 2 <= heap_size:
            if (index * 2 + 1) <= heap_size and self.heap[index * 2 + 1] > self.heap[index * 2]:
                candidate = index * 2 + 1
            else:
                candidate = index * 2
            
            if self.heap[index] < self.heap[candidate]:
                tmp = self.heap[index]
                self.heap[index] = self.heap[candidate]
                self.heap[candidate] = tmp
                index = candidate
            else:
                break
        return 
    
    def build_heap(self):
        for i in range(self.capacity // 2, 0, -1):
            self.heapfy(i, self.capacity)

    def heap_sort(self):
        self.build_heap()
        for i in range(self.capacity, 1, -1):
            tmp = self.heap[1]
            self.heap[1] = self.heap[i]
            self.heap[i] = tmp

            self.heapfy(1, i -1)

    def print_heap(self):
        if self.capacity == 0:
            print("Empty heap")
            return
    
        level = 0
        i = 1
        while i <= self.capacity:
            level_size = 2 ** level
            level_nodes = []
            for j in range(level_size):
                if i + j <= self.capacity:
                    level_nodes.append(str(self.heap[i + j]))
                else:
                    break
            print(f"Level {level}: {' '.join(level_nodes)}")
            i += level_size
            level += 1

    def print_tree(self, index=1, prefix="", is_tail=True):
        if index > self.capacity:
            return
    
        if index * 2 + 1 <= self.capacity:
            self.print_tree(index * 2 + 1, prefix + ("    " if is_tail else "│   "), False)
        
        print(prefix + ("└── " if is_tail else "┌── ") + str(self.heap[index]))
        
        if index * 2 <= self.capacity:
            self.print_tree(index * 2, prefix + ("    " if is_tail else "│   "), True)

