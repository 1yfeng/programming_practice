from collections import defaultdict

class MinWindow:
    def min_window(self, s: str, t: str) -> str:
        if not s or not t :
            return ""
        
        target_char2count = defaultdict(int)
        source_char2count = defaultdict(int)
        for c in t:
            target_char2count[c] += 1
        
        end = 0
        n = len(s)
        min_substring = s + ' '
        for start in range(n):
            while (end < n and
                    not self.__is_covered(source_char2count, target_char2count)):
                source_char2count[s[end]] += 1
                end += 1

            if self.__is_covered(source_char2count, target_char2count) and  (end - start) < len(min_substring):
                min_substring = s[start: end]
            
            source_char2count[s[start]] -= 1
            start += 1

        if len(min_substring) > n:
            return ""
        return min_substring

    def __is_covered(self, source, target) -> bool:
        for key in target:
            if target[key] >  source[key]:
                return False
        return True
    
    #opt: is covered logic, reduce time cost
    def min_window_v2(self, s: str, t: str) -> str:
        if not s or not t :
            return ""
        
        target_char2count = defaultdict(int)
        source_char2count = defaultdict(int)
        for c in t:
            target_char2count[c] += 1
        matched_chars = 0
        
        end = 0
        n = len(s)
        #best to store index not string
        min_substring = s + ' '
        for start in range(n):
            while (end < n and matched_chars < len(target_char2count)):
                source_char2count[s[end]] += 1
                if s[end] in target_char2count and source_char2count[s[end]]  == target_char2count[s[end]] :
                    matched_chars +=1
                end += 1

            if matched_chars == len(target_char2count) and (end - start) < len(min_substring):
                min_substring = s[start: end]
            
            if s[start] in target_char2count and source_char2count[s[start]]  == target_char2count[s[start]] :
                    matched_chars -=1
            source_char2count[s[start]] -= 1
            start += 1

        if len(min_substring) > n:
            return ""
        return min_substring

  
