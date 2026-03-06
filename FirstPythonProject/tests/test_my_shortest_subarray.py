import pytest
from src.algorithm.my_shortest_subarray import MyShortestSubarray
from collections import deque
import heapq
import random

def test_my_shortest_subarray_function():
    shortest_subarray = MyShortestSubarray()
    # input = [64, 40, 49, 73, 72, 35, 68, 83, 35, 73, 84, 88, 96, 43, 74, 63, 41, 95, 48, 46, 89, 72, 34, 85, 72, 59, 87, 49, 30, 32, 47, 34, 74, 58, 31, 75, 73, 88, 64, 92, 83, 64, 100, 99, 81, 41, 48, 83, 96, 92, 82, 32, 35, 68, 68, 92];
    nums = [56,-21,56,35,-9]
    k = 61
    print(f"test__my_shortest_subarray_function {shortest_subarray.shortest_subarray(nums, k)}")


def test_my_shortest_subarray_eg_k_function():
    dq = deque()
    dq.appendleft(1)
    dq.append(2)
    dq.append(3)
    print(f"dq[0]={dq[0]}, dq[1]={dq[1]}")
    print(f"dq.pop()={dq.pop()}")
    print(f"dq.popleft()={dq.popleft()}")
    print(f"len(dq)={len(dq)}")


def test_heap_function():
    heap = MyHeap()

    print()
    for i in range(15):
        heap.delete(i - 8)
        value = random.randint(1, 100)
        print(f"current value={value},index={i}") 


        heap.add(value, i)
        print(f"current value={value},len(heap)={(heap.size())} , delete_set={ ", ".join(str(i) for i in heap.delete_set)}")

class MyHeap:
    def __init__(self):
        self.heap = []
        self.delete_set = set()

    def __lazy_delete(self):
        while self.heap and self.heap[0][1] in self.delete_set:
            self.delete_set.remove(self.heap[0][1])
            heapq.heappop(self.heap)
    
    def add(self, val, index):
        return heapq.heappush(self.heap, (val, index))

    def delete(self, index):
        self.delete_set.add(index)

    def top(self):
        self.__lazy_delete()
        return self.heap[0]
    
    def pop(self):
        self.__lazy_delete()
        return heapq.heappop(self.heap)
    
    def size(self) -> int:
        return len(self.heap)