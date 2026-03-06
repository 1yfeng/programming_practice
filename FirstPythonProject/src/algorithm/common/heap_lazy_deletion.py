import heapq

class HeapLazyDeletion:
    def __init__(self, data):
        self.delete_set = {}
        self.heap = data
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)

    def delete(self, id: int):
        self.delete_set.add(id)
    
    def top(self):
        top_element = self.heap[0]
        while top_element in self.delete_set:
            self.delete_set.remove(top_element)
            heapq.heappop(self.heap)
            top_element = self.heap[0]

        return top_element

    def pop(self):
        while self.heap:
             top_element = heapq.heappop()
             if top_element in self.delete_set:
                self.delete_set.remove(top_element)
                continue
             return top_element
        return None

 


