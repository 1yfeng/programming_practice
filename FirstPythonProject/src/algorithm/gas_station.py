from typing import List
import sys

class GasStation:
    def can_complete_circuit(self, gas:List[int] , cost:List[int]) -> int:
        if not gas or not cost:
            return -1
        
        n = len(gas)
        gain = [0] * n
        prefix_sum = [0]
        # records = []
        max_sum = float('-inf')
        sum = 0
        start = -1
        best_start = -1;
        for i in range(n):
            gain[i] = gas[i] - cost[i]
            prefix_sum.append(prefix_sum[-1] + gain[i])
            
            if start == -1 or prefix_sum[i + 1] < prefix_sum[start]:
                start = i + 1
            

        
        sum = 0
        for i in range(n):
            sum += gain[(i + start) % n]
            if sum < 0:
                return -1
        return best_start

    def can_complete_circuit_v2(self, gas:List[int] , cost:List[int]) -> int:
        if not gas or not cost:
            return -1

        start = 0
        n = len(gas)

        while start < n:
            count = 0 
            gas_sum = 0
            cost_sum = 0
            while count < n:
                gas_sum += gas[(start + count) % n]
                cost_sum += cost[(start + count) % n]
                count += 1
                if gas_sum < cost_sum:
                    break;

            if count == n and gas_sum >= cost_sum:
                return start
            else:
                start += count

        return -1



