from __future__ import annotations

from collections import OrderedDict, defaultdict
import heapq


class LFUCache:
    """Recommended O(1) average-time LFU cache implementation.

    Data structure design:
    - key_to_val_freq: key -> (value, frequency)
    - freq_to_keys: frequency -> OrderedDict of keys for LRU tiebreaking
    - min_freq: current minimum frequency in cache
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq: dict[int, tuple[int, int]] = {}
        self.freq_to_keys: dict[int, OrderedDict[int, None]] = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        value, _ = self.key_to_val_freq[key]
        self._increase_freq(key)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._increase_freq(key)
            return

        if len(self.key_to_val_freq) >= self.capacity:
            self._evict_one()

        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

    def _increase_freq(self, key: int) -> None:
        value, freq = self.key_to_val_freq[key]

        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        new_freq = freq + 1
        self.key_to_val_freq[key] = (value, new_freq)
        self.freq_to_keys[new_freq][key] = None

    def _evict_one(self) -> None:
        keys = self.freq_to_keys[self.min_freq]
        evict_key, _ = keys.popitem(last=False)
        if not keys:
            del self.freq_to_keys[self.min_freq]

        del self.key_to_val_freq[evict_key]


class LFUCacheClassic:
    """Classic heap + lazy-deletion LFU cache.

    Complexity:
    - get / put are O(log n) due to heap maintenance.
    - Simpler to reason about, but not the strict O(1) target.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val: dict[int, int] = {}
        self.key_to_freq: dict[int, int] = {}
        self.key_to_time: dict[int, int] = {}
        self.heap: list[tuple[int, int, int]] = []
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        self._touch(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._touch(key)
            return

        if len(self.key_to_val) >= self.capacity:
            self._evict_one()

        self.time += 1
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.key_to_time[key] = self.time
        heapq.heappush(self.heap, (1, self.time, key))

    def _touch(self, key: int) -> None:
        self.time += 1
        freq = self.key_to_freq[key] + 1
        self.key_to_freq[key] = freq
        self.key_to_time[key] = self.time
        heapq.heappush(self.heap, (freq, self.time, key))

    def _evict_one(self) -> None:
        while self.heap:
            freq, stamp, key = heapq.heappop(self.heap)

            if key not in self.key_to_val:
                continue
            if self.key_to_freq[key] != freq:
                continue
            if self.key_to_time[key] != stamp:
                continue

            del self.key_to_val[key]
            del self.key_to_freq[key]
            del self.key_to_time[key]
            return
