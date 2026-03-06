from typing import List
import math 
class ModernLudo:
    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        if length <= 1:
            return -1
        if not connections:
            return math.ceil((length - 1)/ 6)
        
        sortedList = [[] for _ in range(length + 1)]
        
        for i in range(len(connections)):
            sortedList[connections[i][0]].append((connections[i][0], connections[i][1]))

        count = 0
        position  = 1 
        while position < length:
            count, position =  self.check_connection(position, count, length, sortedList)
        
        return count


    def check_connection(self, position, count: int, length: int, sortedList:list[list[tuple]]) -> tuple[int, int]:
        max_position = position
        for i in range(6):
            if (position + i) > length:
                break
            for pair in sortedList[position + i]:
                if pair[1] > max_position:
                    max_position = pair[1]
            if i == 0 and max_position > position:
                return count, max_position

        if max_position > (position + 6):
            return count + 1, max_position
        else:
            return count + 1, position + 6

