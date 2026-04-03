from  collections  import heapq

class LengthOfLIS:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        max_len = 1
        heap_list = []
        
        for i in range(n):
            pop_list = []
            while heap_list and heapq[0][1] >= nums[i]:
                pop_list.append(heapq.pop(heap_list))
            dp[i] = heapq[0][0] + 1
            heapq.push(heap_list,  (dp[i], nums[i]), key lambda:  x )
    

            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] =max(dp[i], dp[j] + 1)
            if max_len < dp[i]:
                max_len = dp[i]
            #print(f"i, {i}; dp[i], {dp[i]}")
        
        return max_len

    # tails[i]  维护的是 长度为 i+ 1 的递增子序列的最大元素也就最后一个元素的 最小指  例如  length = 2  [1, 5]  tails[1] = 5 before  [1, 3] after  tails[1] = 3 , 
    # 只需要存 长度为x 的 结尾最小，， 为什么能替，， 因为之前已经插入在前，， 而当前在后面 所以可以复用之前的小于它的前缀
    #  
    # O(n log n) 贪心 + 二分
    def lengthOfLIS_bisect(self, nums: List[int]) -> int:
        import bisect
        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
