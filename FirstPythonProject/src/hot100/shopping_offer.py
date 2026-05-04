from typing import List
from functools import cache

class ShoppingOffers:   
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if not needs:
            return 0
        available_packages = []

        n = len(needs)
        
        for p in special:
            offer_count = sum(p[:-1])
            offers_cost = sum(p * need for p, need in zip(price, p[:-1]))
            if offer_count > 0 and offers_cost > p[-1]:
                available_packages.append(p)
        m = len(special)

        @cache
        def dfs(status: tuple[int, ...]) -> int:

            min_cost = sum(p * need for p, need in zip(price, status))
            
            for p in available_packages:
                new_status = []
                for i in range(n):
                    if p[i] > status[i]:
                        break
                    
                    new_status.append(status[i] - p[i])   
                else:
                    min_cost = min(min_cost, dfs(tuple(new_status)) + p[-1])
                
            return min_cost
        
        return dfs(tuple(needs))