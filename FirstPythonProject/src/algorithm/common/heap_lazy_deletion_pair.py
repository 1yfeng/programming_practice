import heapq

class HeapLazyDeletionPair:
    def __init__(self, data = []):
        self.delete_set = set()
        self.heap = data
      
    def heapify(self):
        heapq.heapify(self.heap)

    def push(self, val, index):
        heapq.heappush(self.heap, (val, index))

    def delete(self, id: int):
        self.delete_set.add(id)

    def _lazy_delete(self):
        while self.heap and self.heap[0][1] in self.delete_set:
            val, index = heapq.heappop(self.heap)
            self.delete_set.remove(index)
    
    def top(self):
        self._lazt_delete()
        return self.heap[0]

    def pop(self):
        self._lazt_delete()
        return heapq.heappop(self.heap)