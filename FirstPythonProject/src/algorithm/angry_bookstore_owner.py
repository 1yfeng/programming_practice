from typing import List 

class AngryBookstoreOwner:
    def max_satisfied(self, customers: List[int], grumpy: List[int], minutes: int) ->int :
        if not customers or not grumpy or len(customers) != len(grumpy):
            return 0
        
        n = len(customers)
        static_satisfied= [0] * n
        try_satisfied= [0] * n
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 1:
                try_satisfied[i] = customers[i]
            else:
                satisfied += customers[i]
                static_satisfied[i] = customers[i]
      
        minutes_satisfied = 0
        for i in range(minutes):
            minutes_satisfied += try_satisfied[i]
        max_satisfied = minutes_satisfied
        for i in range(minutes, n, 1):
            #i - minutes > 0 ;   i - minutes == -1  no error 
            minutes_satisfied += (try_satisfied[i] - try_satisfied[i - minutes])
            if max_satisfied < minutes_satisfied:
                max_satisfied = minutes_satisfied
        
        return satisfied + max_satisfied
