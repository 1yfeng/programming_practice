from typing import List
from collections import defaultdict
class WordSquares:
    def word_squares(self, words: List[str]) -> List[List[str]]:
        if not words or not words[0]:
            return None
        
        matrix = []
        visited = set()
        result = []
        word_len = len(words[0])
        records = [set()] * word_len
        for j in range(len(words[0])):
            for i in range(len(words)):
                records[j].add(words[i][j])

        self.dfs(words, matrix, visited, records, result)
        return result

    def dfs(self, words: List[str], matrix: list[int], visited: set[int], records: list[set[str]], result: List[List[str]]):
        target = len(words[0])
        height = len(matrix)

        if height == target:
            chekc_result = self.check_vaild(words, matrix)
            if chekc_result:
                result.append(chekc_result)
            return 
        prefix_list = []
        for i in range(height):
            prefix_list.append(words[matrix[i]][height])
        prefix = "".join(prefix_list)

        n = len(words)
        for i in range(n):
            if i in visited:
                continue
            skip = False
            for j in range(target):
                if words[i][j] not in records[height]:
                    skip = True
                    break
            if skip:
                continue

            if words[i].startswith(prefix):
                matrix.append(i)
                visited.add(i)
                self.dfs(words, matrix, visited, records, result)
                visited.remove(i)
                matrix.remove(i)
        return

    def check_vaild(self,  words: List[str], matrix: list[int]) ->  List[List[str]]:
        n = len(words[0])
        result = []
        for i in range(n):
            word = []
            for j in range(n):
                word.append(words[matrix[j]][i])
            if ("".join(word)) == words[matrix[i]]:
                result.append(words[matrix[i]])
            else:
                return None
        
        return result

            
    def word_squares_2(self, words: List[str]) -> List[List[str]]:
        if not words or not words[0]:
            return None
        
        matrix = []
        result = []
        word_len = len(words[0])
        records = defaultdict(list)

        for i in range(len(words)):
            for j in range(word_len):
                records[words[i][:j+1]].append(words[i])
        
        self.dfs_2(words, matrix,  records, result)
        return result
    
    def dfs_2(self, words: List[str], matrix: list[str], records: list[set[str]], result: List[List[str]]):
        target = len(words[0])
        height = len(matrix)

        if height == target:
            result.append(matrix)
            return 
        
        prefix_list = []
        for i in range(height):
            prefix_list.append(matrix[i][height])
        prefix = "".join(prefix_list)

        n = len(words)
        canidate = None
        if height == 0:
            canidate = words
        else:
            canidate = records[prefix]
        for s in canidate:
            matrix.append(s)
            self.dfs_2(words, matrix, records, result)
            # bug remove ?
            matrix.pop()

        return
    
    # unsless, can remove 
    # why ?  当你用前2行或者3行的  3,4 列去找匹配的前缀 就已经限定了  第二行的后缀 和第二列的后缀匹配
    # 因为第一二列的后缀就是第三四行的前！！！！！！！！！ 所以用前缀匹配找的结果不用在check 检查没查的后缀是否匹配 它们已经包含在剩下行的前缀检查过了
    def check_vaild_2(self,  words: List[str], matrix: list[int]) ->  List[List[str]]:
        n = len(words[0])
        result = []
        for i in range(n):
            word = []
            for j in range(n):
                word.append(matrix[j][i])
            if ("".join(word)) == matrix[i]:
                result.append(matrix[i])
            else:
                return None
        
        return result