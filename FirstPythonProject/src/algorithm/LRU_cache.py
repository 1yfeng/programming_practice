class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.key2count = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        val = self.store.get(key, -1)
        if val != -1:
            self.key2count[key] += self.key2count[key] + 1
        return val

    def put(self, key: int, value: int) -> None:
        if len(self.store) + 1 < self.capacity