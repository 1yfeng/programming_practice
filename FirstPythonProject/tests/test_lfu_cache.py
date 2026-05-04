import pytest

from src.algorithm.lfu_cache import LFUCache, LFUCacheClassic


@pytest.mark.parametrize("cache_cls", [LFUCache, LFUCacheClassic])
def test_lfu_leetcode_example(cache_cls):
    cache = cache_cls(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)  # evicts key=2
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    cache.put(4, 4)  # evicts key=1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


@pytest.mark.parametrize("cache_cls", [LFUCache, LFUCacheClassic])
def test_lfu_tie_break_by_lru(cache_cls):
    cache = cache_cls(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  # freq tie at 1, evict older key=1

    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3


@pytest.mark.parametrize("cache_cls", [LFUCache, LFUCacheClassic])
def test_lfu_put_existing_updates_and_counts_as_use(cache_cls):
    cache = cache_cls(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # update key=1 and increase its frequency
    cache.put(3, 3)  # should evict key=2

    assert cache.get(1) == 10
    assert cache.get(2) == -1
    assert cache.get(3) == 3


@pytest.mark.parametrize("cache_cls", [LFUCache, LFUCacheClassic])
def test_lfu_capacity_zero(cache_cls):
    cache = cache_cls(0)

    cache.put(1, 1)
    assert cache.get(1) == -1
