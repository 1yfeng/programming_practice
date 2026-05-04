from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.key_2_value: dict[int, tuple[int, int]] = {}
        self.count_2_keys: dict[int, OrderedDict] = defaultdict(OrderedDict)
        self.capacity = capacity
        self.min_count = 0

    def _increase_count(self, key: int) -> None:
        value, count = self.key_2_value[key]
        del self.count_2_keys[count][key]
        if not self.count_2_keys[count]:
            del self.count_2_keys[count]
            if self.min_count == count:
                self.min_count += 1
        self.key_2_value[key] = (value, count + 1)
        self.count_2_keys[count + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_2_value:
            return -1
        value, _ = self.key_2_value[key]
        self._increase_count(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_2_value:
            _, count = self.key_2_value[key]
            self.key_2_value[key] = (value, count)   # 先更新值，_increase_count 会读它
            self._increase_count(key)
            return

        if len(self.key_2_value) >= self.capacity:
            keys = self.count_2_keys[self.min_count]
            evict_key, _ = keys.popitem(last=False)
            if not keys:
                del self.count_2_keys[self.min_count]
            del self.key_2_value[evict_key]

        self.key_2_value[key] = (value, 1)
        self.count_2_keys[1][key] = None
        self.min_count = 1











if __name__ == "__main__":
    d = {4:2}
    node = BiNode(0)

    print(d.get(4))
    del d[4]
    print(d.get(4))