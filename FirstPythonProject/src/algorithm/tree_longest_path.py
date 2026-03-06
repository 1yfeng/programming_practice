from typing import List
import collections

class TreeLongestPath:
    def TreeLongestPath(self, n: int, starts: List[int], ends: List[int], lens: List[int]) -> int:
        if not starts or not ends or not lens:
            return -1
        
        start_dict = collections.defaultdict(dict)
        for i in range(len(starts)):
            start_dict[starts[i]][ends[i]] = lens[i]

        print()
        for k in start_dict:
            for k_k in start_dict[k]:
                print(f"start={k}, end = {k_k}, len = {start_dict[k][k_k]}")

        
        return -1
                

if __name__ == "__main__":
    t = TreeLongestPath()
    t.TreeLongestPath(n=5,starts=[0,0,2,2],ends=[1,2,3,4],lens=[1,2,5,6])
