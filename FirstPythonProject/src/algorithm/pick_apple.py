class PickApple:
    def pick(self, trees: list[int], k: int, l :int) -> int:
        if not trees:
            return 0
        
        n = len(trees)
        max_num = 0
        for i in range(n):
            left_k = self.__get_apple_num(trees, 0, i, k)
            left_l = self.__get_apple_num(trees, 0, i, l)
            right_k = self.__get_apple_num(trees, i, n, k)
            right_l = self.__get_apple_num(trees, i, n, l)
            max_num = max(max_num, left_k + right_l, left_l + right_k)
        
        return max_num


    def __get_apple_num(self, trees: list[int], start: int , end: int, target: int) -> int:
        if target > end - start:
            return 0 
        
        max_num, sum = 0 , 0
        for i in range(start, end, 1):
            if i < target:
                sum += trees[i]
                max_num = sum
            else:
                sum += (trees[i] - trees[i - target])
                max_num = max(max_num, sum)
        return max_num
