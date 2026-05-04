class Soluation:
    def getModifiedArray(length: int, updates: list[list[int]]) -> list[int]:
        if length <= 0:
            return []
        
        result = [0] * length
        if not updates:
            return result
        n = len(updates)
        
        for i in range(n):
            for j in range(updates[i][0], updates[i][1] + 1, 1):
                result[j] +=  updates[i][2]

        return result 

    def getModifiedArray_v2(length: int, updates: list[list[int]]) -> list[int]:
        if length <= 0:
            return []
        
        result = [0] * length
        diff = [0] * length
        if not updates:
            return result
        n = len(updates)
        for i in range(n):
            diff[updates[i][0]] += updates[i][2]
            diff[updates[i][1] + 1] -= updates[i][2]
        prefix_sum = 0
        for i in range(length):
            prefix_sum += diff[i]
            result[i] = prefix_sum
        
        


        return result 
