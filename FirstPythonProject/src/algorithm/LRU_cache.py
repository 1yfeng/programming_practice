import heapq
from datetime import datetime

# what is LRU?  del which ? how pick
#put is a visited ,need update flag
class LRUCache:
 
    def __init__(self, capacity: int):
        self.store = {}
        self.key2count = {}
        self.capacity = capacity
 
    def get(self, key: int) -> int:
        val = self.store.get(key, -1)
        if val != -1:
            self.key2count[key] = f"{datetime.now()}"
        return val
 
    def put(self, key: int, value: int) -> None:
        if len(self.store) < self.capacity and key not in self.store:
            self.store[key] = value

        elif len(self.store)  == self.capacity and key not in self.store:
            key_list = heapq.nsmallest(1, self.key2count.items(), key=lambda x : x[1])
            self.store.pop(key_list[0][0])
            self.key2count.pop(key_list[0][0])
            self.store[key] = value

        else:
            self.store[key] = value

        self.key2count[key] = f"{datetime.now()}"

